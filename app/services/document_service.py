import hashlib
import shutil
from pathlib import Path

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.indexing.indexing_service import index_document
from app.indexing.vector_store import delete_document_chunks
from app.models.collection import Collection
from app.models.document import Document


class DocumentService:

    def __init__(self, db: Session):
        self.db = db

    def calculate_file_hash(
        self,
        file_path: Path,
    ) -> str:

        sha256 = hashlib.sha256()

        with open(file_path, "rb") as file:

            while chunk := file.read(8192):
                sha256.update(chunk)

        return sha256.hexdigest()

    def upload_document(
        self,
        collection_id: int,
        file: UploadFile,
    ):

        collection = (
            self.db.query(Collection)
            .filter(
                Collection.id == collection_id
            )
            .first()
        )

        if not collection:

            raise HTTPException(
                status_code=404,
                detail="Collection not found",
            )

        upload_path = Path(
            settings.DOCUMENT_DIR
        )

        upload_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        destination = (
            upload_path /
            file.filename
        )

        with destination.open("wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer,
            )

        file_hash = self.calculate_file_hash(
            destination
        )

        existing = (
            self.db.query(Document)
            .filter(
                Document.file_hash == file_hash
            )
            .first()
        )

        if existing:

            destination.unlink(
                missing_ok=True
            )

            raise HTTPException(
                status_code=409,
                detail="Document already exists",
            )

        document = Document(

            filename=file.filename,

            filepath=str(destination),

            file_hash=file_hash,

            status="uploading",

            collection_id=collection_id,

        )

        try:

            self.db.add(document)

            self.db.commit()

            self.db.refresh(document)

            chunk_count = index_document(
                document
            )

            document.status = "indexed"

            self.db.commit()

            self.db.refresh(document)

            print(
                f"Indexed {chunk_count} chunks."
            )

            return document

        except Exception as e:

            self.db.rollback()

            if destination.exists():

                destination.unlink()

            if document.id is not None:

                self.db.query(Document).filter(
                    Document.id == document.id
                ).delete()

                self.db.commit()

            raise HTTPException(
                status_code=500,
                detail=f"Document indexing failed: {e}",
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

            raise HTTPException(
                status_code=404,
                detail="Document not found",
            )

        delete_document_chunks(
            document.id
        )

        file_path = Path(
            document.filepath
        )

        if file_path.exists():

            file_path.unlink()

        self.db.delete(
            document
        )

        self.db.commit()

        return {
            "message": "Document deleted successfully"
        }