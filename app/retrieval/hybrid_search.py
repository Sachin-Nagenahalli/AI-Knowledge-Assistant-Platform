from app.retrieval.vector_search import (
    VectorSearch,
)

from app.retrieval.bm25_search import (
    BM25Search,
)

from app.retrieval.fusion import (
    Fusion,
)

from app.retrieval.reranker import (
    CrossEncoderReranker,
)


class HybridSearch:

    def __init__(self):

        self.vector = VectorSearch()

        self.bm25 = BM25Search()

        self.fusion = Fusion()

        self.reranker = CrossEncoderReranker()

    def search(
        self,
        query: str,
        collection_id: int,
    ):

        print("\n" + "=" * 70)
        print("HYBRID SEARCH")
        print("=" * 70)

        # -----------------------------
        # Vector Search
        # -----------------------------
        vector_results = self.vector.search(
            query=query,
            collection_id=collection_id,
        )

        print(
            f"Vector Search returned {len(vector_results['ids'][0])} chunks"
        )

        # -----------------------------
        # BM25 Search
        # -----------------------------
        bm25_results = self.bm25.search(
            query=query,
            collection_id=collection_id,
        )

        print(
            f"BM25 returned {len(bm25_results)} chunks"
        )

        # -----------------------------
        # Reciprocal Rank Fusion
        # -----------------------------
        ranking = self.fusion.fuse(
            vector_results,
            bm25_results,
        )

        print("\nTop RRF Results")

        for item in ranking[:10]:
            print(item)

        # -----------------------------
        # Cross Encoder (placeholder)
        # -----------------------------
        reranked = self.reranker.rerank(
            query=query,
            results=ranking,
        )

        print("=" * 70)

        # IMPORTANT:
        # We still return the Chroma results
        # because Retriever expects the Chroma format.
        return vector_results