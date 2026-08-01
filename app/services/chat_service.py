from app.rag.engine import RAGEngine
from app.services.memory_service import MemoryService


memory = MemoryService()


class ChatService:

    def __init__(self):
        self.engine = RAGEngine()

    def ask(
        self,
        collection_id: int,
        question: str,
    ):

        memory.add_user(question)

        result = self.engine.ask(
            collection_id=collection_id,
            question=question,
        )

        memory.add_assistant(
            result.answer
        )

        return {
            "answer": result.answer,
            "sources": [
                {
                    "filename": source.filename,
                    "document_id": source.document_id,
                    "collection_id": source.collection_id,
                    "chunk": source.chunk,
                    "score": source.score,
                }
                for source in result.sources
            ],
            "confidence": result.confidence,
        }