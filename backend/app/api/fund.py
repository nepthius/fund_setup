from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.fund import FundCreate, FundOut
from app.services.fund import create_fund, get_fund, generate_ppm, get_funds, generate_lpa, generate_sub, generate_form_d_preview
from app.services.docgen import render_legal_doc
from app.db.session import get_db
from app.services.blue_sky import generate_blue_sky_state_summary
from fastapi.responses import PlainTextResponse, StreamingResponse
from io import BytesIO
from typing import List



router = APIRouter()

#fund routes
@router.post("/funds", response_model = FundOut)
def create_fund_route(fund: FundCreate, db:Session = Depends(get_db)):
    return create_fund(db, fund)

@router.post("/funds/more", response_model=List[FundOut])
def create_funds_route_more(funds: List[FundCreate], db: Session = Depends(get_db)):
    return [create_fund(db, fund) for fund in funds]

@router.get("/funds/{fund_name}", response_model = FundOut)
def find_fund(fund_name:str, db: Session = Depends(get_db)):
    fund = get_fund(db, fund_name)
    if not fund:
        raise HTTPException(status_code=404, detail="Fund not found")
    return fund

@router.get("/funds", response_model=list[FundOut])
def grab_all_funds(db: Session = Depends(get_db)):
    funds = get_funds(db)
    return funds

'''
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
'''

@router.get("/funds/{fund_name}/generate/{doc_type}", response_class=StreamingResponse)
def generate_doc_pdf(fund_name: str, doc_type: str, db: Session = Depends(get_db)):
    fund = get_fund(db, fund_name)
    if not fund:
        raise HTTPException(status_code=404, detail="Fund not found")

    template_map = {
        "ppm": "ppm_template.md",
        "lpa": "lpa_template.md",
        "sub": "sub_template.md"
    }

    if doc_type not in template_map:
        raise HTTPException(status_code=400, detail="Invalid document type.")

    pdf_bytes = render_legal_doc(template_map[doc_type], fund)
    buffer = BytesIO(pdf_bytes)
    filename = f"{fund.name}_{doc_type}.pdf"

    return StreamingResponse(buffer, media_type="application/pdf", headers={
        "Content-Disposition": f"attachment; filename={filename}"
    })


@router.get("/funds/{fund_name}/generate/form_d")
def generate_form_d_doc(fund_name: str, db: Session = Depends(get_db)):
    fund = get_fund(db,fund_name)
    return generate_form_d_preview(fund)

@router.get("/funds/{fund_name}/blue_sky_summary")
def blue_sky_summary(fund_name: str, db: Session = Depends(get_db)):
    return generate_blue_sky_state_summary(fund_name, db)
