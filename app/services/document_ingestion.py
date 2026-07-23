from pathlib import Path

from sqlalchemy.orm import Session

from app.repositories.document_repository import (
    create_document,
    create_document_chunk,
)
from app.services.embeddings import EmbeddingService
from app.services.ingest import IngestionService


class DocumentIngestionService:

    def __init__(
        self,
        ingestion_service: IngestionService,
        embedding_service: EmbeddingService,
    ) -> None:

        self.ingestion_service = ingestion_service
        self.embedding_service = embedding_service

    def ingest_pdf(
        self,
        db: Session,
        pdf_path: str | Path,
    ) -> None:
        try:
            text = self.ingestion_service.extract_text(pdf_path)
            chunks = self.ingestion_service.chunk_text(text)
            embeddings = self.embedding_service.embed_batch(chunks)
            document = create_document(db=db, filename=Path(pdf_path).name)
            db.flush()  # Ensure document.id is populated before creating chunks
            for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
                create_document_chunk(
                    db=db,
                    document_id=document.id,
                    chunk_index=index,
                    content=chunk,
                    embedding=embedding,
                )
            db.commit()  # Commit the transaction to save the document and its chunks
        except Exception as e:
            db.rollback()  # Rollback the transaction in case of an error
            raise e  # Re-raise the exception for further handling