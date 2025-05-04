from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.investor import InvestorCreate, InvestorOut
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
    

@router.get("/investors/by_fund/{fund_name}")
def get_investor_by_fund(fund_name: str, db: Session = Depends(get_db)):
    return db.query(Investor).filter(fund_name == Investor.fund_name).all()

@router.get("/investors/{investor_id}", response_model = InvestorOut)
def get_investor(investor_id: int, db: Session = Depends(get_db)):
    inv = db.get(Investor,investor_id)
    if not inv:
        raise HTTPException(status_code=404, detail="Investor not found")
    return inv