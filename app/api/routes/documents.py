from fastapi import APIRouter

from app.db.queries import create_document
from app.schemas.document import DocumentCreate, DocumentResponse


router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/", response_model=DocumentResponse)
def create_document_endpoint(document: DocumentCreate):
    return create_document(document.filename)