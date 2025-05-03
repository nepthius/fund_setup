from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.fund import FundCreate, FundOut
from app.services.fund import create_fund, get_fund
from app.db.session import get_db

router = APIRouter()

@router.post("/funds", response_model = FundOut)
def create_fund_route(fund: FundCreate, db:Session = Depends(get_db)):
    return create_fund(db, fund)

@router.get("/funds/{fund_name}", response_model = FundOut)
def find_fund(fund_name:str, db: Session = Depends(get_db)):
    fund = get_fund(db, fund_name)
    if not fund:
        raise HTTPException(status_code=404, detail="Fund not found")
    return fund

