from pathlib import Path


def build_metadata(
    document,
    chunk_id: int,
    chunk_text: str,
):
    """
    Build metadata for each semantic chunk.
    """

    filename = Path(
        document.filename
    ).name

    metadata = {
        "document_id": document.id,
        "collection_id": document.collection_id,
        "filename": filename,
        "chunk": chunk_id,
        "word_count": len(
            chunk_text.split()
        ),
        "character_count": len(
            chunk_text
        ),
    }

    return metadata
    