from pydantic import BaseModel


class ChatRequest(BaseModel):
    collection_id: int
    question: str


class ChatResponse(BaseModel):
    answer: str
    sources: list