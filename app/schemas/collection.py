from pydantic import BaseModel
from datetime import datetime


class CollectionCreate(BaseModel):
    name: str
    description: str | None = None


class CollectionResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
    