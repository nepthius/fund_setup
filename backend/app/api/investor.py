from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.investor import InvestorCreate
from app.db.session import get_db
from app.models.investor import Investor

router = APIRouter()

@router.post("/investors")
def add_investor(investor: InvestorCreate, db: Session = Depends(get_db)):
    db_investor = Investor(**investor.dict())
    db.add(db_investor)
    db.commit()
    db.refresh(db_investor)
    return db_investor

@router.get("/investors")
def get_investors(db: Session = Depends(get_db)):
    return db.query(Investor).all()
    

@router.get("/investors/{fund_name}")
def get_investor_by_fund(fund_name: str, db: Session = Depends(get_db)):
    return db.query(Investor).filter(fund_name == Investor.fund_name).all()

