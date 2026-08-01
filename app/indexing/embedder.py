import ollama

from app.core.config import settings


client = ollama.Client(
    host=settings.OLLAMA_URL
)


def create_embedding(text: str):
    """
    Generate an embedding using the configured
    Ollama embedding model.
    """

    if not text:
        raise ValueError(
            "Cannot create embedding from empty text."
        )

    text = text.strip()

    if len(text) == 0:
        raise ValueError(
            "Cannot create embedding from blank text."
        )

    try:

        response = client.embed(
            model=settings.EMBEDDING_MODEL,
            input=text,
        )

    except Exception as e:

        raise RuntimeError(
            f"Ollama embedding request failed: {e}"
        )

    embeddings = response.get(
        "embeddings",
        []
    )

    if not embeddings:

        raise RuntimeError(
            f"Embedding model '{settings.EMBEDDING_MODEL}' returned no embeddings."
        )

    embedding = embeddings[0]

    if not embedding:

        raise RuntimeError(
            "Received an empty embedding vector."
        )

    return embedding