from collections import defaultdict
from sqlalchemy.orm import Session

def generate_blue_sky_state_summary(fund_name: str, db: Session):
    from app.models.investor import Investor
    investors = db.query(Investor).filter(Investor.fund_name == fund_name).all()
    states = defaultdict(int)

    count = 0

    for inv in investors:
        if inv.state not in states:
            count+=1
        states[inv.state] +=1

    return {
        "total_states": count,
        "states": states
    }
