from sqlalchemy import text

from app.db.database import engine


def create_document(filename: str):
    query = text("""
        INSERT INTO documents (filename)
        VALUES (:filename)
        RETURNING id, filename, uploaded_at;
    """)

    with engine.begin() as conn:
        result = conn.execute(query, {"filename": filename})
        return result.mappings().first()
    
    
def create_document_chunk(
    document_id: int,
    chunk_index: int,
    content: str,
    embedding: list[float],
) -> None:
    """
    Insert a document chunk and its embedding into the database.

    Args:
        document_id: Parent document ID.
        chunk_index: Position of the chunk.
        content: Chunk text.
        embedding: Embedding vector.
    """

    query = text("""
        INSERT INTO document_chunks
        (
            document_id,
            chunk_index,
            content,
            embedding
        )
        VALUES
        (
            :document_id,
            :chunk_index,
            :content,
            :embedding
        );
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "document_id": document_id,
                "chunk_index": chunk_index,
                "content": content,
                "embedding": embedding,
            },
        )