import hashlib
import shutil
from pathlib import Path

from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logger import logger
from app.models.document import Document
from app.models.collection import Collection


class DocumentService:

    def __init__(self, db: Session):
        self.db = db

    def upload_document(self, file_path: str, collection_name: str):
        pass

    def list_documents(self):
        pass

    def delete_document(self, document_id: int):
        pass

    def get_document(self, document_id: int):
        pass