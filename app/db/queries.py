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