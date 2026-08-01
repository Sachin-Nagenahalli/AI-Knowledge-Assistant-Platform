from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.collection import (
    CollectionCreate,
    CollectionResponse,
)
from app.services.collection_service import CollectionService

router = APIRouter(
    prefix="/collections",
    tags=["Collections"],
)


@router.post(
    "",
    response_model=CollectionResponse,
)
def create_collection(
    data: CollectionCreate,
    db: Session = Depends(get_db),
):

    service = CollectionService(db)

    return service.create_collection(data)


@router.get(
    "",
    response_model=list[CollectionResponse],
)
def list_collections(
    db: Session = Depends(get_db),
):

    service = CollectionService(db)

    return service.list_collections()


@router.delete(
    "/{collection_id}",
)
def delete_collection(
    collection_id: int,
    db: Session = Depends(get_db),
):

    service = CollectionService(db)

    return service.delete_collection(
        collection_id
    )