from fastapi import APIRouter, Query

from app.services.search_service import SearchService

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)

service = SearchService()


@router.get("")
def search(
    query: str = Query(...),
    collection_id: int = Query(...),
):
    return service.search(
        query=query,
        collection_id=collection_id,
    )