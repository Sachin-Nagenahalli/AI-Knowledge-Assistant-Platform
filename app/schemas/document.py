from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DocumentResponse(BaseModel):
    id: int
    filename: str
    filepath: str
    file_hash: str
    status: str
    collection_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)