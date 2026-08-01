from app.rag.vector_search import VectorSearch

from app.rag.models import (
    Chunk,
    RetrievalResult,
)


class Retriever:

    def __init__(self):

        self.vector = VectorSearch()

    def retrieve(
        self,
        query: str,
        collection_id: int,
    ):

        results = self.vector.search(
            query=query,
            collection_id=collection_id,
        )

        retrieval = RetrievalResult(
            query=query
        )

        for item in results:

            retrieval.chunks.append(

                Chunk(

                    id=item["id"],

                    text=item["text"],

                    metadata=item["metadata"],

                    score=item["score"],

                )

            )

        return retrieval
        