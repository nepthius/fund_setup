from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.chat import query_chat
from app.schemas.chat import ChatRequest


router = APIRouter()

@router.post("/chat")
def chat_api(req: ChatRequest, db: Session = Depends(get_db)):
    answer = query_chat(req.message, db)
    return {"response": answer}