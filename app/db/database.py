from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from app.core.config import settings


engine: Engine = create_engine(
    settings.DATABASE_URL,
    echo=True,          # Print SQL queries (great for learning)
    pool_pre_ping=True, # Automatically checks dead connections
)