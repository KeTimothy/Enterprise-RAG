from app.database.connection import Base, engine
from app.database import models

print("Tables:", Base.metadata.tables.keys())

for name, table in Base.metadata.tables.items():
    print(f"Table: {name}")
    print(table)

print("About to create_all")

Base.metadata.create_all(bind=engine)

print("Done")