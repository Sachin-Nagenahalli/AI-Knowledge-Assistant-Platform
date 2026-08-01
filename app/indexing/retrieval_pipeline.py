from app.core.chroma import get_collection
from app.indexing.embedder import create_embedding


class RetrievalPipeline:

    def __init__(self):

        self.collection = get_collection(
            "documents"
        )

    def retrieve(
        self,
        query: str,
        collection_id: int,
        top_k: int = 20,
    ):
        """
        Retrieve candidate chunks from ChromaDB.
        """

        embedding = create_embedding(
            query
        )

        results = self.collection.query(
            query_embeddings=[
                embedding
            ],
            n_results=top_k,
            where={
                "collection_id": collection_id
            },
        )

        return results

    def merge_chunks(
        self,
        results,
    ):
        """
        Placeholder for context expansion.

        Version 1 simply returns the retrieved
        chunks. Later versions will merge
        neighbouring chunks automatically.
        """

        return results

    def rerank(
        self,
        results,
    ):
        """
        Placeholder for reranking.

        Currently returns the retrieved order.

        Future:
            Cross Encoder
            BGE Reranker
            Jina AI Reranker
        """

        return results

    def build_context(
        self,
        results,
        top_n: int = 3,
    ):
        """
        Build the final context that will be
        sent to the LLM.
        """

        documents = results["documents"][0]

        context = "\n\n".join(
            documents[:top_n]
        )

        return context

    def run(
        self,
        query: str,
        collection_id: int,
    ):
        """
        Complete retrieval pipeline.
        """

        results = self.retrieve(
            query=query,
            collection_id=collection_id,
            top_k=20,
        )

        results = self.merge_chunks(
            results
        )

        results = self.rerank(
            results
        )

        context = self.build_context(
            results
        )

        return context, results