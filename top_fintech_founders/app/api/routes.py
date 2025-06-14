from fastapi import APIRouter, Query
from typing import List
from app.models.founder import FounderOut
from app.services.embeddings import search_top_founders

router = APIRouter()

@router.get("/top-founders", response_model=List[FounderOut])
def get_top_founders(query: str = Query("fintech inovação"), top_k: int = 20):
    return search_top_founders(query, top_k)
