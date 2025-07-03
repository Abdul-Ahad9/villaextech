from sqlalchemy import Column, Integer, String, Text, ForeignKey, Numeric, DateTime, func
from sqlalchemy.orm import relationship
from database import Base  # Assuming you have a `Base` from `declarative_base()`


class Work(Base):
    __tablename__ = "works"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    content = Column(Text, nullable=False)
    artist_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    artist = relationship("User", back_populates="works")
    supports = relationship("Support", back_populates="work")


class Support(Base):    
    __tablename__ = "supports"

    id = Column(Integer, primary_key=True, index=True)
    work_id = Column(Integer, ForeignKey("works.id"), nullable=False)
    supporter_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Numeric, nullable=False)
    supported_at = Column(DateTime(timezone=True), server_default=func.now())

    work = relationship("Work", back_populates="supports")
    supporter = relationship("User", back_populates="supports")
