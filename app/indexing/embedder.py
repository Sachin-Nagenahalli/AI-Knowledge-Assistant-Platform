import ollama

from app.core.config import settings


def create_embedding(text: str):
    response = ollama.embed(
        model=settings.EMBEDDING_MODEL,
        input=text,
    )

    return response.embeddings[0]