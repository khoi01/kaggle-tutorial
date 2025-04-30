from sqlalchemy import Column,Integer,String,ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer,primary_key=True)
    title = Column(String(150),nullable=False)
    content = Column(String,nullable=False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    
    user = relationship("User", back_populates="posts")
    