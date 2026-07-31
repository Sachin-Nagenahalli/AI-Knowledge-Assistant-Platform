from fastapi import FastAPI
# Register SQLAlchemy models
from app.models.collection import Collection
from app.models.document import Document
from app.api.collection import router as collection_router
from app.core.config import settings
from app.api.document import router as document_router
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Knowledge Platform"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(collection_router)
app.include_router(document_router)