from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central configuration for the application.
    Values can be overridden from the .env file.
    """

    # ==========================
    # Project Settings
    # ==========================
    PROJECT_NAME: str = "AI Knowledge Platform"
    API_VERSION: str = "v1"

    # ==========================
    # Storage Paths
    # ==========================
    SQLITE_DB_PATH: str = "storage/app.db"
    CHROMA_DB_PATH: str = "data/chroma_db"

    UPLOAD_DIR: str = "data/uploads"
    DOCUMENT_DIR: str = "data/documents"

    # ==========================
    # Ollama Settings
    # ==========================
    OLLAMA_URL: str = "http://host.docker.internal:11434"

    LLM_MODEL: str = "qwen2.5:3b"
    EMBEDDING_MODEL: str = "embeddinggemma"

    # ==========================
    # RAG Settings
    # ==========================
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    TOP_K: int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()