from fastapi import APIRouter
from app.services.nlp_router import route_intent
from app.services.ehr import generate_ehr_summary
from app.services.logger import log_symptom_query
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class Query(BaseModel):
    text: str

@router.get("/ping")
def ping():
    return {"status": "running"}

@router.post("/route")
def route_user_query(query: Query):
    intent = route_intent(query.text)
    log_symptom_query(query.text, intent, datetime.now())
    return {"intent": intent}

@router.get("/ehr/summary")
def get_summary():
    return {"summary": generate_ehr_summary()}
