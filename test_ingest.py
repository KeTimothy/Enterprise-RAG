from app.services.ingest import ingestion_service
from app.services.embeddings import embedding_service

text = ingestion_service.extract_text("./data/nvidia_annual_report_2025.pdf")

chunks = ingestion_service.chunk_text(text, chunk_size=500, chunk_overlap=100)

embeddings = embedding_service.embed_batch(chunks)

assert len(chunks) == len(embeddings)