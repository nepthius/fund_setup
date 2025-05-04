from fastapi import FastAPI
from app.api import fund, investor

app = FastAPI()
app.include_router(fund.router, prefix="/api", tags=["funds"]) #<- adds all the "fun"d stuff 
app.include_router(investor.router, prefix="/api", tags=["investors"])
