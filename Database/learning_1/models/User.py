from sqlalchemy import Column,Integer,String
from db.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)
    email = Column(String(120),nullable=False)
    
    posts = relationship("Post", back_populates="user", cascade="all, delete-orphan")
