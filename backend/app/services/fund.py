from sqlalchemy.orm import Session
from app.models.fund import Fund
from app.schemas.fund import FundCreate

def create_fund(db: Session, fund_in:FundCreate) -> Fund:
    fund = Fund(**fund_in.dict())
    db.add(fund)
    db.commit()
    db.refresh(fund)
    return fund

def get_fund(db:Session, fund_name: str) -> Fund:
    return db.query(Fund).filter(Fund.name == fund_name).first()