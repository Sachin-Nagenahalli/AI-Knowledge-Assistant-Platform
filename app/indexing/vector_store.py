from app.core.chroma import get_collection


collection = get_collection("documents")


def store_chunks(document_id: int, chunks: list[str]):
    ids = []
    embeddings = []
    documents = []
    metadatas = []

    from app.indexing.embedder import create_embedding

    for index, chunk in enumerate(chunks):
        ids.append(f"{document_id}_{index}")
        embeddings.append(create_embedding(chunk))
        documents.append(chunk)

        metadatas.append(
            {
                "document_id": document_id,
                "chunk": index,
            }
        )

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas,
    )