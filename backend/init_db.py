from app.db.session import engine
from app.db.base import Base

print("Creating database...")
Base.metadata.create_all(bind=engine)
print("Done.")
