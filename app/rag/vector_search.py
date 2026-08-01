from app.core.chroma import get_collection
from app.indexing.embedder import create_embedding


class VectorSearch:

    def __init__(self):

        self.collection = get_collection(
            "documents"
        )

    def search(
        self,
        query: str,
        collection_id: int,
        top_k: int = 20,
        similarity_threshold: float = 0.35,
    ):

        embedding = create_embedding(query)

        results = self.collection.query(

            query_embeddings=[
                embedding
            ],

            n_results=top_k,

            where={
                "collection_id": collection_id
            }

        )

        filtered = []

        for chunk_id, text, metadata, distance in zip(

            results["ids"][0],
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],

        ):

            score = round(
                1 - distance / 2,
                3,
            )

            if score >= similarity_threshold:

                filtered.append({

                    "id": chunk_id,

                    "text": text,

                    "metadata": metadata,

                    "score": score,

                })

        filtered.sort(

            key=lambda x: x["score"],

            reverse=True,

        )

        return filtered[:5]