from pydantic import BaseModel
from typing import Optional
import enum

class FundType(str, enum.Enum):
    PRIVATE_EQUITY = "Private Equity"
    PRIVATE_CREDIT = "Private Credit"
    SPV = "SPV"

class ExemptionType(str, enum.Enum):
    RULE_506B = "506(b)"
    RULE_506C = "506(c)"
    REG_A = "Reg A"
    REG_S = "Reg S"
    RULE_4A2 = "4(a)(2)"

#this schema is helpful for validating data when it comes in to check if it is what is expected
class FundCreate(BaseModel):
    name:str
    type:FundType
    manager: str
    management_fee: float
    carry: float
    jurisdiction: Optional[str] = "Delaware"
    total_raise: Optional[float]
    min_investment: Optional[float]
    exemption: Optional[ExemptionType]
    manager_contact_email: Optional[str]

#what the fund creation returns, and orm_mode just means to read like fund.id and not fund["id"]
class FundOut(FundCreate):
    name:str
    type:FundType
    manager: str
    management_fee: float
    carry: float
    jurisdiction: Optional[str]
    total_raise: Optional[float]
    min_investment: Optional[float]
    exemption: Optional[ExemptionType]
    manager_contact_email: Optional[str]
    #right now it's basically the same as the fund type minus the id, but later on if there's confidential info, I'm leaving it for masking 

    class Config:
        orm_mode = True