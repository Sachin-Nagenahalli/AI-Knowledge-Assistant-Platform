from fastapi import APIRouter

from app.services.search_service import SearchService

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)

service = SearchService()


@router.get("")
def search(
    query: str,
):
    return service.search(query)