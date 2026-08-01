from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.services.document_management_service import (
    DocumentManagementService,
)

router = APIRouter(
    prefix="/documents",
    tags=["Document Management"],
)


@router.get("")
def list_documents(
    db: Session = Depends(get_db),
):
    service = DocumentManagementService(db)

    return service.list_documents()


@router.get("/collection/{collection_id}")
def list_collection_documents(
    collection_id: int,
    db: Session = Depends(get_db),
):
    service = DocumentManagementService(db)

    return service.list_collection_documents(
        collection_id
    )


@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    service = DocumentManagementService(db)

    return service.delete_document(document_id)