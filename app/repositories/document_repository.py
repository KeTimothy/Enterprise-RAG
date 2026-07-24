from pgvector.sqlalchemy import Vector
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Document, DocumentChunk


def create_document(
    db: Session,
    filename: str,
) -> Document:
    """
    Create a new document in the database.

    Args:
        db (Session): The database session.
        filename (str): The filename of the document.

    Returns:
        Document: The created document.
    """
    
    document = Document(filename=filename)

    db.add(document)

    return document

def create_document_chunk(
    db: Session,
    document_id: int,
    chunk_index: int,
    content: str,
    embedding: list[float],
) -> DocumentChunk:
    """
    Create a new document chunk in the database.

    Args:
        db (Session): The database session.
        document_id (int): The ID of the document to which the chunk belongs.
        chunk_index (int): The index of the chunk within the document.
        content (str): The content of the chunk.
        embedding (list[float]): The embedding vector for the chunk.

    Returns:
        DocumentChunk: The created document chunk.
    """

    chunk = DocumentChunk(
        document_id=document_id,
        chunk_index=chunk_index,
        content=content,
        embedding=embedding,
    )

    db.add(chunk)

    return chunk

def search_similar_chunks(
    db: Session,
    query_embedding: list[float],
    top_k: int = 5,
) -> list[DocumentChunk]:
    """
    Search for the most similar document chunks based on the provided embedding.

    Args:
        db (Session): The database session.
        query_embedding (list[float]): The embedding vector to search against.
        top_k (int): The number of top similar chunks to return.

    Returns:
        list[DocumentChunk]: A list of the most similar document chunks.
    """
    stmt = (
        select(DocumentChunk)
        .order_by(DocumentChunk.embedding.cosine_distance(query_embedding))
        .limit(top_k)
    )
    return list(db.scalars(stmt))