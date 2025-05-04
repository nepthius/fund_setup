from fastapi import FastAPI
from app.api import fund, investor
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#adding this so that the frontend can make calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fund.router, prefix="/api", tags=["funds"]) #<- adds all the "fun"d stuff 
app.include_router(investor.router, prefix="/api", tags=["investors"])
