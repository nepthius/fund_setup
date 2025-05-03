from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.fund import FundCreate, FundOut
from app.services.fund import create_fund, get_fund, generate_ppm, get_funds, generate_lpa, generate_sub
from app.db.session import get_db
from fastapi.responses import PlainTextResponse

router = APIRouter()

#fund routes
@router.post("/funds", response_model = FundOut)
def create_fund_route(fund: FundCreate, db:Session = Depends(get_db)):
    return create_fund(db, fund)

@router.get("/funds/{fund_name}", response_model = FundOut)
def find_fund(fund_name:str, db: Session = Depends(get_db)):
    fund = get_fund(db, fund_name)
    if not fund:
        raise HTTPException(status_code=404, detail="Fund not found")
    return fund

@router.get("/funds", response_model=list[str])
def grab_all_funds(db: Session = Depends(get_db)):
    funds = get_funds(db)
    return funds

#doc generations
@router.get("/funds/{fund_name}/generate/ppm", response_class = PlainTextResponse)
def generate_ppm_doc(fund_name: str, db: Session = Depends(get_db)):
    fund = get_fund(db, fund_name)
    ppm = generate_ppm(fund)
    return ppm

@router.get("/funds/{fund_name}/generate/lpa", response_class = PlainTextResponse)
def generate_lpa_doc(fund_name: str, db: Session = Depends(get_db)):
    fund = get_fund(db, fund_name)
    lpa = generate_lpa(fund)
    return lpa

@router.get("/funds/{fund_name}/generate/sub", response_class = PlainTextResponse)
def generate_sub_doc(fund_name: str, db: Session = Depends(get_db)):
    fund = get_fund(db, fund_name)
    sub = generate_sub(fund)
    return sub