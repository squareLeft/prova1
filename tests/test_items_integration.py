from pathlib import Path

from fastapi.testclient import TestClient

from app.main import create_app


def test_items_crud_flow(tmp_path: Path) -> None:
    db_path = tmp_path / "integration.sqlite3"
    app = create_app(f"sqlite:///{db_path}")

    with TestClient(app) as client:
        create_response = client.post(
            "/items",
            json={"name": "example", "description": "first item"},
        )
        assert create_response.status_code == 201
        created = create_response.json()
        assert created["id"] > 0
        assert created["name"] == "example"

        list_response = client.get("/items")
        assert list_response.status_code == 200
        assert len(list_response.json()) == 1

        item_id = created["id"]
        get_response = client.get(f"/items/{item_id}")
        assert get_response.status_code == 200
        assert get_response.json()["description"] == "first item"

        update_response = client.put(
            f"/items/{item_id}",
            json={"description": "updated"},
        )
        assert update_response.status_code == 200
        assert update_response.json()["description"] == "updated"

        delete_response = client.delete(f"/items/{item_id}")
        assert delete_response.status_code == 204

        missing_response = client.get(f"/items/{item_id}")
        assert missing_response.status_code == 404
