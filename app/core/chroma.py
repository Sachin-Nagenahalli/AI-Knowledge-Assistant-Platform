import chromadb

from app.core.config import settings


client = chromadb.PersistentClient(
    path=settings.CHROMA_DB_PATH
)


def get_collection(name: str):
    """
    Get an existing collection or create it if it doesn't exist.
    """
    return client.get_or_create_collection(name=name)