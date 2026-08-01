from app.core.chroma import get_collection

collection = get_collection("documents")


def store_chunks(document, chunks):
    ids = []
    embeddings = []
    documents = []
    metadatas = []

    from app.indexing.embedder import create_embedding

    for index, chunk in enumerate(chunks):
        ids.append(f"{document.id}_{index}")

        embeddings.append(
            create_embedding(chunk)
        )

        documents.append(chunk)

        metadatas.append(
            {
                "document_id": document.id,
                "collection_id": document.collection_id,
                "chunk": index,
                "filename": document.filename,
            }
        )

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas,
    )


def delete_document_chunks(document_id: int):
    """
    Delete all vector embeddings belonging to one document.
    """

    results = collection.get(
        where={
            "document_id": document_id
        }
    )

    ids = results.get("ids", [])

    if ids:
        collection.delete(
            ids=ids
        )