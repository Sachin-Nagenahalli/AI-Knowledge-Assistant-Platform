from app.core.database import Base, engine

# Import all models
from app.models.collection import Collection
from app.models.document import Document

Base.metadata.create_all(bind=engine)

print("Database created successfully!")