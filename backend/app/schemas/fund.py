from pydantic import BaseModel
from typing import Optional
from datetime import date
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
    term_years: Optional[int] = 7
    subscription_deadline: Optional[date]
    capital_call_notice_days: Optional[int] = 10
    preferred_return: Optional[float]
    org_expense_cap: Optional[float] = 100000.0
    admin_fee_percent: Optional[float]
    initial_close_date: Optional[date]
    asset_focus: Optional[str] = "private equity"
    target_sectors: Optional[str]

#what the fund creation returns, and orm_mode just means to read like fund.id and not fund["id"]
class FundOut(FundCreate):
    model_config = {
        "from_attributes": True
    }
    #right now it's basically the same as the fund type minus the id, but later on if there's confidential info, I'm leaving it for masking 