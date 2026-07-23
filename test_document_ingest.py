from app.db.database import SessionLocal
from app.services.document_ingestion import DocumentIngestionService
from app.services.embeddings import embedding_service
from app.services.ingest import ingestion_service


def main():
    db = SessionLocal()

    service = DocumentIngestionService(
        ingestion_service=ingestion_service,
        embedding_service=embedding_service,
    )

    try:
        service.ingest_pdf(
            db=db,
            pdf_path="data/employee_handbook.pdf",
        )

        print("✅ Document ingested successfully!")

    finally:
        db.close()


if __name__ == "__main__":
    main()