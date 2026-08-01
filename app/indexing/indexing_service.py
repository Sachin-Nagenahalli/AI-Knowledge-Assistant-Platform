from app.indexing.chunker import chunk_text
from app.indexing.pdf_loader import extract_text
from app.indexing.vector_store import store_chunks


def index_document(document):
    text = extract_text(
        document.filepath
    )

    chunks = chunk_text(text)

    store_chunks(
        document,
        chunks,
    )