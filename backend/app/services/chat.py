from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.schema import Document
from llama_index.llms.openai import OpenAI
from sqlalchemy.orm import Session
from app.models.investor import Investor
from app.models.fund import Fund
from dotenv import load_dotenv
import os
load_dotenv()
llm = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def build_documents_from_db(db: Session):
    docs = []
    investors = db.query(Investor).all()
    for inv in investors:
        docs.append(Document(text=f"Investor {inv.name} committed to fund {inv.fund_name} with amount {inv.investment_amount}. Accredited: {inv.accredited}. State: {inv.state}. Status: {inv.kyc_status}"))

    funds = db.query(Fund).all()
    for fund in funds:
        docs.append(Document(text=f"Fund {fund.name} is a {fund.type} based in {fund.jurisdiction}. Manager: {fund.manager}. Management fee: {fund.management_fee}, carry: {fund.carry}"))

    return docs

def query_chat(prompt: str, db: Session):
    documents = build_documents_from_db(db)
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine(llm=llm, similarity_top_k=100) #<-- adding 100 so I don't hit the 2 limitation problem when asking bout people
    response = query_engine.query(prompt)
    return str(response)
