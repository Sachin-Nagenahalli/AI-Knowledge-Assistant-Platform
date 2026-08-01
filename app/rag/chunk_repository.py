from app.core.chroma import get_collection


class ChunkRepository:

    def __init__(self):

        self.collection = get_collection(
            "documents"
        )

    def get_chunk(
        self,
        document_id: int,
        chunk: int,
    ):

        results = self.collection.get(
            where={
                "document_id": document_id,
                "chunk": chunk,
            },
            include=[
                "documents",
                "metadatas",
            ],
        )

        if len(results["documents"]) == 0:
            return None

        return {
            "text": results["documents"][0],
            "metadata": results["metadatas"][0],
        }
        