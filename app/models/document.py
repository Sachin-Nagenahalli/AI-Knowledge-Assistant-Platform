from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    filepath = Column(String, nullable=False)

    file_hash = Column(String, unique=True, nullable=False)

    status = Column(String, default="uploaded")

    collection_id = Column(
        Integer,
        ForeignKey("collections.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    collection = relationship(
        "Collection",
        back_populates="documents"
    )