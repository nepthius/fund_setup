from fastapi import FastAPI
from app.api import fund

app = FastAPI()
app.include_router(fund.router, prefix="/api", tags=["funds"]) #<- adds all the "fun"d stuff 

