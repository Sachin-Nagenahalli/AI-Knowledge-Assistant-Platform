from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

service = ChatService()


@router.post("")
def chat(request: ChatRequest):

    if not request.question.strip():

        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty.",
        )

    return service.ask(
        request.collection_id,
        request.question.strip(),
    )