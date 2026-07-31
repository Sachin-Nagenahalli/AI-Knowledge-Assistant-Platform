from fastapi import APIRouter

router = APIRouter(
    prefix="/collections/{collection_id}/documents",
    tags=["Documents"],
)
