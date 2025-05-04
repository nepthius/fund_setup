from pydantic import BaseModel
from typing import Optional

class InvestorCreate(BaseModel):
    name: str
    state: str
    email: str
    fund_name: str