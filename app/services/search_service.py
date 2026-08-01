from app.core.chroma import get_collection
from app.indexing.embedder import create_embedding


class SearchService:

    def __init__(self):
        self.collection = get_collection("documents")

    def search(
        self,
        query: str,
        collection_id: int,
        top_k: int = 5,
    ):

        embedding = create_embedding(query)

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
            where={
                "collection_id": collection_id
            }
        )

        return results