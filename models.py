from sqlalchemy import Column, Integer, String, DateTime, func
from db import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    contact_number = Column(String)
    user_name = Column(String)
    product_name = Column(String)
    product_review = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
