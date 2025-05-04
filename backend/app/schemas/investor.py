from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import date

class InvestorCreate(BaseModel):
    name: str
    state: str
    email: EmailStr
    fund_name: str
    accredited: Optional[bool] = False
    kyc_status: Optional[str] = "pending" 
    subscription_status: Optional[str] = "not_started"
    investment_amount: Optional[float] = None
    date_committed: Optional[date] = None
    notes: Optional[str] = None

class InvestorOut(InvestorCreate):
    id: int 

    model_config = ConfigDict(from_attributes=True)