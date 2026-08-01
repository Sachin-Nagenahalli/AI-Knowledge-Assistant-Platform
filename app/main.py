from fastapi import FastAPI
import ollama

from app.api.chat import router as chat_router
from app.api.collection import router as collection_router
from app.api.document import router as document_router
from app.api.document_management import router as document_management_router
from app.api.search import router as search_router
from app.core.chroma import get_collection
from app.core.database import engine


app = FastAPI(
    title="AI Knowledge Platform",
    version="1.0.0",
    description="Local RAG API built with FastAPI, ChromaDB, SQLite, and Ollama",
)


# ============================
# Routers
# ============================

app.include_router(collection_router)
app.include_router(document_router)
app.include_router(document_management_router)
app.include_router(search_router)
app.include_router(chat_router)


# ============================
# Root
# ============================

@app.get("/")
def root():

    return {
        "message": "AI Knowledge Platform API is running successfully!"
    }


# ============================
# Health Check
# ============================

@app.get("/health")
def health():

    health = {
        "status": "healthy",
        "database": "disconnected",
        "chroma": "disconnected",
        "ollama": "disconnected",
    }

    # SQLite
    try:

        connection = engine.connect()
        connection.close()

        health["database"] = "connected"

    except Exception:

        pass

    # Chroma
    try:

        get_collection("documents")

        health["chroma"] = "connected"

    except Exception:

        pass

    # Ollama
    try:

        ollama.ps()

        health["ollama"] = "connected"

    except Exception:

        pass

    if (
        health["database"] == "connected"
        and health["chroma"] == "connected"
        and health["ollama"] == "connected"
    ):

        health["status"] = "healthy"

    else:

        health["status"] = "degraded"

    return health