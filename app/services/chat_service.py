import ollama

from app.core.config import settings
from app.services.search_service import SearchService


class ChatService:
    def __init__(self):
        self.search = SearchService()

    def ask(self, question: str):
        results = self.search.search(question)

        context = "\n\n".join(
            results["documents"][0]
        )

        prompt = f"""
You are an AI assistant.

Answer ONLY from the provided context.

If the answer is not found in the context, reply exactly:

I could not find that information in the uploaded documents.

Context:

{context}

Question:

{question}
"""

        response = ollama.chat(
            model=settings.LLM_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return {
            "answer": response.message.content,
            "sources": results["metadatas"][0]
        }