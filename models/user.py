from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base  # Assuming you have a `Base` from `declarative_base()`

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    works = relationship("Work", back_populates="artist")
    supports = relationship("Support", back_populates="supporter")