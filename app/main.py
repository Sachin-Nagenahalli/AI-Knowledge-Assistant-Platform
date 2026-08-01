from fastapi import FastAPI

from app.api.collection import router as collection_router
from app.api.document import router as document_router
from app.api.search import router as search_router
from app.api.chat import router as chat_router
from app.api.document_management import router as document_management_router

app = FastAPI(
    title="AI Knowledge Platform",
    version="1.0.0",
    description="Local RAG API built with FastAPI, ChromaDB, SQLite, and Ollama",
)

# Collection APIs
app.include_router(collection_router)

# Document Upload APIs
app.include_router(document_router)

# Document Management APIs
app.include_router(document_management_router)

# Semantic Search APIs
app.include_router(search_router)

# AI Chat APIs
app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "AI Knowledge Platform API is running successfully!"
    }