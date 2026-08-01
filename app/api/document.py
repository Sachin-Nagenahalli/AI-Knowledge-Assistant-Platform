from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService

router = APIRouter(
    tags=["Documents"],
)


# ----------------------------
# Upload Document
# ----------------------------

@router.post(
    "/collections/{collection_id}/documents/upload",
    response_model=DocumentResponse,
)
def upload_document(
    collection_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    service = DocumentService(db)

    return service.upload_document(
        collection_id=collection_id,
        file=file,
    )


# ----------------------------
# List Documents
# ----------------------------

@router.get(
    "/documents",
    response_model=list[DocumentResponse],
)
def list_documents(
    db: Session = Depends(get_db),
):
    return (
        db.query(
            __import__("app.models.document", fromlist=["Document"]).Document
        )
        .all()
    )


# ----------------------------
# Delete Document
# ----------------------------

@router.delete(
    "/documents/{document_id}",
)
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    service = DocumentService(db)

    return service.delete_document(
        document_id
    )