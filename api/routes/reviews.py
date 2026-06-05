from fastapi import APIRouter
from database import supabase
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class Review(BaseModel):
    reviewer_name: str
    review_text: str
    stars: int

@router.get("/")
def get_reviews():
    res = supabase.table("reviews").select("*").eq("is_active", True).order("created_at", desc=True).execute()
    return res.data

@router.post("/")
def add_review(r: Review):
    # Auto-generate initials from name
    parts = r.reviewer_name.strip().split()
    initials = ''.join([p[0].upper() for p in parts[:2]])
    
    from datetime import datetime
    date_label = datetime.now().strftime("%d %b %Y")

    data = {
        "reviewer_name": r.reviewer_name,
        "initials": initials,
        "review_text": r.review_text,
        "stars": r.stars,
        "date_label": date_label,
        "is_active": True
    }
    res = supabase.table("reviews").insert(data).execute()
    return res.data