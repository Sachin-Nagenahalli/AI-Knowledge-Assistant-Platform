from app.core.config import settings


def chunk_text(text: str):
    chunks = []

    start = 0

    while start < len(text):
        end = start + settings.CHUNK_SIZE

        chunks.append(text[start:end])

        start += settings.CHUNK_SIZE - settings.CHUNK_OVERLAP

    return chunks
    