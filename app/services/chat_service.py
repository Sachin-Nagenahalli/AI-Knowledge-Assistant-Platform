import ollama

from app.core.config import settings
from app.services.search_service import SearchService
from app.services.memory_service import MemoryService


memory = MemoryService()


class ChatService:
    def __init__(self):
        self.search = SearchService()

    def ask(self, question: str):
        # Search relevant chunks
        results = self.search.search(question)

        context = "\n\n".join(
            results["documents"][0]
        )

        # Save current user message
        memory.add_user(question)

        # Build conversation
        messages = [
            {
                "role": "system",
                "content": f"""
You are an AI assistant.

Answer ONLY from the provided context.

If the answer is not found in the context, reply exactly:

I could not find that information in the uploaded documents.

Context:

{context}
"""
            }
        ]

        # Add previous conversation
        messages.extend(memory.history())

        # Ask the LLM
        response = ollama.chat(
            model=settings.LLM_MODEL,
            messages=messages
        )

        answer = response.message.content

        # Save assistant response
        memory.add_assistant(answer)

        sources = []

        for metadata, distance in zip(
            results["metadatas"][0],
            results["distances"][0]
        ):
            sources.append(
                {
                    "filename": metadata["filename"],
                    "document_id": metadata["document_id"],
                    "chunk": metadata["chunk"],
                    "score": round(1 - distance / 2, 3)
                }
            )

        return {
            "answer": answer,
            "sources": sources
                }