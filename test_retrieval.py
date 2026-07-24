from app.db.database import SessionLocal
from app.repositories.document_repository import search_similar_chunks
from app.services.embeddings import EmbeddingService

embedding_service = EmbeddingService()

embedding = embedding_service.embed_query(
    "What is the annual leave policy?"
)

with SessionLocal() as db:
    chunks = search_similar_chunks(
        db=db,
        query_embedding=embedding,
        top_k=3,
    )

for chunk in chunks:
    print(f"Chunk ID: {chunk.id}, Content: {chunk.content}")
    print("-" * 50)