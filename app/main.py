from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import DEFAULT_DATABASE_URL, create_sqlite_engine, get_session_factory
from app.models import Base, Item
from app.schemas import ItemCreate, ItemRead, ItemUpdate


def create_app(database_url: str = DEFAULT_DATABASE_URL) -> FastAPI:
    engine = create_sqlite_engine(database_url)
    Base.metadata.create_all(bind=engine)
    get_session = get_session_factory(engine)

    app = FastAPI(title="SQLAlchemy 2.x + SQLite example")

    @app.post("/items", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
    def create_item(payload: ItemCreate, session: Session = Depends(get_session)) -> Item:
        existing = session.scalar(select(Item).where(Item.name == payload.name))
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An item with this name already exists.",
            )

        item = Item(name=payload.name, description=payload.description)
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

    @app.get("/items", response_model=list[ItemRead])
    def list_items(session: Session = Depends(get_session)) -> list[Item]:
        return list(session.scalars(select(Item).order_by(Item.id)).all())

    @app.get("/items/{item_id}", response_model=ItemRead)
    def get_item(item_id: int, session: Session = Depends(get_session)) -> Item:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found.")
        return item

    @app.put("/items/{item_id}", response_model=ItemRead)
    def update_item(
        item_id: int,
        payload: ItemUpdate,
        session: Session = Depends(get_session),
    ) -> Item:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found.")

        if payload.name is not None:
            item.name = payload.name
        if payload.description is not None:
            item.description = payload.description

        session.add(item)
        session.commit()
        session.refresh(item)
        return item

    @app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_item(item_id: int, session: Session = Depends(get_session)) -> None:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found.")

        session.delete(item)
        session.commit()
        return None

    return app


app = create_app()
