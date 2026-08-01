import os

from sqlalchemy.orm import Session

from app.models.document import Document
from app.core.chroma import get_collection


class DocumentManagementService:

    def __init__(self, db: Session):
        self.db = db
        self.collection = get_collection("documents")

    def list_documents(self):
        return self.db.query(Document).all()

    def list_collection_documents(
        self,
        collection_id: int,
    ):
        return (
            self.db.query(Document)
            .filter(
                Document.collection_id == collection_id
            )
            .all()
        )

    def delete_document(
        self,
        document_id: int,
    ):
        document = (
            self.db.query(Document)
            .filter(
                Document.id == document_id
            )
            .first()
        )

        if not document:
            return {
                "message": "Document not found"
            }

        # Delete PDF file
        if os.path.exists(document.filepath):
            os.remove(document.filepath)

        # Delete vectors from ChromaDB
        self.collection.delete(
            where={
                "document_id": document.id
            }
        )

        # Delete database record
        self.db.delete(document)
        self.db.commit()

        return {
            "message": "Document deleted successfully"
        }