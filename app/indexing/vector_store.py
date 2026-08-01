from app.core.chroma import get_collection
from app.indexing.embedder import create_embedding
from app.indexing.metadata import build_metadata


collection = get_collection("documents")


def store_chunks(
    document,
    chunks,
):
    """
    Generate embeddings and store chunks in ChromaDB.
    """

    records = []

    for index, chunk in enumerate(chunks):

        chunk = chunk.strip()

        if not chunk:
            continue

        embedding = create_embedding(chunk)

        metadata = build_metadata(
            document=document,
            chunk_id=index,
            chunk_text=chunk,
        )

        records.append(
            {
                "id": f"{document.id}_{index}",
                "embedding": embedding,
                "document": chunk,
                "metadata": metadata,
            }
        )

    if not records:

        raise RuntimeError(
            "No valid chunks available for indexing."
        )

    collection.add(
        ids=[r["id"] for r in records],
        embeddings=[r["embedding"] for r in records],
        documents=[r["document"] for r in records],
        metadatas=[r["metadata"] for r in records],
    )


def delete_document_chunks(
    document_id: int,
):
    """
    Remove all chunks belonging to a document.
    """

    results = collection.get(
        where={
            "document_id": document_id
        }
    )

    ids = results.get(
        "ids",
        []
    )

    if ids:

        collection.delete(
            ids=ids
        )