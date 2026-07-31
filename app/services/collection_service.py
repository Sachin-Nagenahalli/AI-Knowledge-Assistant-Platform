from sqlalchemy.orm import Session

from app.models.collection import Collection
from app.schemas.collection import CollectionCreate


class CollectionService:
    def __init__(self, db: Session):
        self.db = db

    def create_collection(self, data: CollectionCreate):
        collection = Collection(
            name=data.name,
            description=data.description
        )

        self.db.add(collection)
        self.db.commit()
        self.db.refresh(collection)

        return collection

    def list_collections(self):
        return self.db.query(Collection).all()

    def get_collection(self, collection_id: int):
        return (
            self.db.query(Collection)
            .filter(Collection.id == collection_id)
            .first()
        )

    def delete_collection(self, collection_id: int):
        collection = self.get_collection(collection_id)

        if not collection:
            return None

        self.db.delete(collection)
        self.db.commit()

        return collection