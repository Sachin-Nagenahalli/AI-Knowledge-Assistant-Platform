import chromadb

client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_or_create_collection(
    "documents"
)

collection.add(
    ids=["1"],
    documents=["hello world"],
    embeddings=[[0.1] * 768],
    metadatas=[{"test": 1}],
)

print("SUCCESS")