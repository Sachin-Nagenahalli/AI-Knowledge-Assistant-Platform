from app.indexing.pdf_loader import extract_text
from app.indexing.semantic_chunker import semantic_chunk
from app.indexing.vector_store import store_chunks


def index_document(document):
    """
    Complete document indexing pipeline.

    Steps:
        1. Extract text from PDF
        2. Create semantic chunks
        3. Store embeddings in ChromaDB
    """

    # -------------------------
    # Extract Text
    # -------------------------

    text = extract_text(
        document.filepath
    )

    if not text.strip():

        raise RuntimeError(
            "No text could be extracted from the PDF."
        )

    # -------------------------
    # Semantic Chunking
    # -------------------------

    chunks = semantic_chunk(
        text
    )

    if len(chunks) == 0:

        raise RuntimeError(
            "Semantic chunker produced no chunks."
        )

    # -------------------------
    # Store in Vector Database
    # -------------------------

    store_chunks(
        document=document,
        chunks=chunks,
    )

    return len(chunks)