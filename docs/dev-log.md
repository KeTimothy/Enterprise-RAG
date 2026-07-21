## 16-07-2026
- Port conflict with local PostgreSQL (both 5432)
- Resolution: Docker PostgreSQL moved to 5433

## 18-07-2026
- Added SQLAlchemy engine
- Implemented POST /documents
- Added response validation
- Verified inserts through Swagger and DBeaver

## 21-07-2026
- Update database schema ($document_chunks$ have 'embedding' now)
- Implemented text ingestion and chunking (with document ingestion pipeline next on the list)