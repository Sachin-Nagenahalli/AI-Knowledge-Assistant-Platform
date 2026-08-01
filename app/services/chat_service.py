import ollama

from app.core.config import settings
from app.services.search_service import SearchService
from app.services.memory_service import MemoryService


memory = MemoryService()


class ChatService:

    def __init__(self):
        self.search = SearchService()

    def ask(
        self,
        collection_id: int,
        question: str,
    ):

        # Search only inside the selected collection
        results = self.search.search(
            query=question,
            collection_id=collection_id,
        )

        context = "\n\n".join(
            results["documents"][0]
        )

        # Save user message
        memory.add_user(question)

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

        # Previous conversation
        messages.extend(
            memory.history()
        )

        response = ollama.chat(
            model=settings.LLM_MODEL,
            messages=messages,
        )

        answer = response.message.content

        # Save assistant reply
        memory.add_assistant(answer)

        sources = []

        for metadata, distance in zip(
            results["metadatas"][0],
            results["distances"][0],
        ):

            sources.append(
                {
                    "filename": metadata.get("filename"),
                    "document_id": metadata.get("document_id"),
                    "collection_id": metadata.get("collection_id"),
                    "chunk": metadata.get("chunk"),
                    "score": round(
                        1 - distance / 2,
                        3,
                    ),
                }
            )

        return {
            "answer": answer,
            "sources": sources,
        }