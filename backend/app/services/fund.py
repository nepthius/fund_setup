from sqlalchemy.orm import Session
from app.models.fund import Fund
from app.schemas.fund import FundCreate
from app.services.docgen import render_legal_doc

def create_fund(db: Session, fund_in:FundCreate) -> Fund:
    fund = Fund(**fund_in.dict())
    db.add(fund)
    db.commit()
    db.refresh(fund)
    return fund

def get_fund(db:Session, fund_name: str) -> Fund:
    return db.query(Fund).filter(Fund.name == fund_name).first()

def get_funds(db:Session) -> list[Fund]:
    res = db.query(Fund.name).all()
    ret = []
    for val in res:
        ret.append(val[0])
    return ret

def generate_ppm(fund) -> str:
    fund_data = {
        "name": fund.name,
        "jurisdiction": fund.jurisdiction,
        "type": fund.type.value,
        "manager": fund.manager,
        "management_fee": fund.management_fee,
        "carry": fund.carry
    }
    return render_legal_doc("ppm_template.md", fund_data)

def generate_lpa(fund) -> str:
    fund_data = {
        "name": fund.name,
        "jurisdiction": fund.jurisdiction,
        "type": fund.type.value,
        "manager": fund.manager,
        "management_fee": fund.management_fee,
        "carry": fund.carry
    }
    return render_legal_doc("lpa_template.md", fund_data)

def generate_sub(fund) -> str:
    fund_data = {
        "name": fund.name,
        "jurisdiction": fund.jurisdiction,
        "type": fund.type.value,
        "manager": fund.manager,
        "management_fee": fund.management_fee,
        "carry": fund.carry
    }
    return render_legal_doc("sub_template.md", fund_data)


def generate_form_d_preview(fund):
    return {
        "issuer_name": fund.name,
        "jurisdiction": fund.jurisdiction,
        "offering_type": fund.type.value,
        "total_raise": fund.total_raise,
        "min_investment": fund.min_investment,
        "exemption": fund.exemption,
        "manager_contact_email": fund.manager_contact_email
    }
