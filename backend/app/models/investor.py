from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float, Date, Text
from app.db.base_class import Base

class Investor(Base):
    __tablename__ = "investors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    state = Column(String, nullable=False)
    email = Column(String)
    fund_name = Column(String, ForeignKey("funds.name"), nullable=False)
    accredited = Column(Boolean, default=False)
    kyc_status = Column(String, default="pending")  # pending, verified, failed
    subscription_status = Column(String, default="not_started")  # not_started, in_progress, signed
    investment_amount = Column(Float, nullable=True)
    date_committed = Column(Date, nullable=True)
    notes = Column(Text, nullable=True)