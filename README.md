# Prova1 API

Esempio minimale con **FastAPI + SQLAlchemy 2.x + SQLite**.

## Avvio locale

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoint CRUD di esempio

- `POST /items`
- `GET /items`
- `GET /items/{item_id}`
- `PUT /items/{item_id}`
- `DELETE /items/{item_id}`

## Test di integrazione

```bash
pytest -q
```
