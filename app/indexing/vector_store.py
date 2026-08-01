from app.core.chroma import get_collection
from app.indexing.embedder import create_embedding
from app.indexing.metadata import build_metadata


collection = get_collection("documents")


def store_chunks(document, chunks):

    records = []

    print("=" * 80)
    print("Starting indexing...")
    print("Chunks received:", len(chunks))

    for index, chunk in enumerate(chunks):

        chunk = chunk.strip()

        if not chunk:
            continue

        print(f"Embedding chunk {index}...")

        embedding = create_embedding(chunk)

        print("Embedding length:", len(embedding))

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

    print("Total records:", len(records))

    print("Calling collection.add()...")

    collection.add(
        ids=[r["id"] for r in records],
        embeddings=[r["embedding"] for r in records],
        documents=[r["document"] for r in records],
        metadatas=[r["metadata"] for r in records],
    )

    print("collection.add() SUCCESS")


def delete_document_chunks(document_id: int):

    results = collection.get(
        where={
            "document_id": document_id
        }
    )

    ids = results.get("ids", [])

    if ids:
        collection.delete(ids=ids)