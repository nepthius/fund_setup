from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from app.db.base_class import Base
import enum

class FundType(str, enum.Enum): #basically enum.Enum and str to behave like both (PRIAVATE_EQUITY=="Private Equity")
    PRIVATE_EQUITY = "Private Equity"
    PRIVATE_CREDIT = "Private Credit"
    SPV = "SPV"

class ExemptionType(str, enum.Enum):
    RULE_506B = "506(b)"
    RULE_506C = "506(c)"
    REG_A = "Reg A"
    REG_S = "Reg S"
    RULE_4A2 = "4(a)(2)"

class Fund(Base): #pass in base to recog that class is a table model
    __tablename__ = "funds"
    id = Column(Integer, primary_key=True, index=True) #index kinda unnecessary since primary key already indexes
    name = Column(String, nullable=False, index=True, unique=True)
    type = Column(Enum(FundType), nullable=False)
    manager = Column(String, nullable=False)
    management_fee = Column(Float, default=2.0)
    carry = Column(Float, default=20.0)
    jurisdiction = Column(String, default="Delaware")
    total_raise = Column(Float, nullable=True)
    min_investment = Column(Float, nullable=True)
    exemption = Column(Enum(ExemptionType), default=ExemptionType.RULE_506B)
    manager_contact_email = Column(String, nullable=True)
