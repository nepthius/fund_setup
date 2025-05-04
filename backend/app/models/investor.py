from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base_class import Base

class Investor(Base):
    __tablename__ = "investors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    state = Column(String, nullable=False)
    email = Column(String)
    fund_name = Column(String, ForeignKey("funds.name"), nullable=False)