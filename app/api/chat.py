from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

service = ChatService()


@router.post("")
def chat(request: ChatRequest):
    return service.ask(request.question)