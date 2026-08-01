from app.retrieval.hybrid_search import HybridSearch

from app.rag.models import (
    Chunk,
    RetrievalResult,
)


class Retriever:

    def __init__(self):

        self.search = HybridSearch()

    def retrieve(
        self,
        query: str,
        collection_id: int,
    ):

        results = self.search.search(

            query=query,

            collection_id=collection_id,

        )

        retrieval = RetrievalResult(
            query=query
        )

        documents = results["documents"][0]

        metadatas = results["metadatas"][0]

        distances = results["distances"][0]

        ids = results["ids"][0]

        for chunk_id, text, metadata, distance in zip(

            ids,

            documents,

            metadatas,

            distances,

        ):

            retrieval.chunks.append(

                Chunk(

                    id=chunk_id,

                    text=text,

                    metadata=metadata,

                    score=round(
                        1 - distance / 2,
                        3,
                    ),

                )

            )

        return retrieval