from fastapi import APIRouter, HTTPException
from database import supabase
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(req: LoginRequest):
    if req.username == ADMIN_USERNAME and req.password == ADMIN_PASSWORD:
        return {"success": True, "token": "maa-chef-admin-authenticated"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/reviews")
def get_reviews():
    res = supabase.table("reviews").select("*").execute()
    return res.data

@router.post("/reviews")
def add_review(review: dict):
    res = supabase.table("reviews").insert(review).execute()
    return res.data

@router.delete("/reviews/{id}")
def delete_review(id: int):
    res = supabase.table("reviews").update({"is_active": False}).eq("id", id).execute()
    return {"message": "Review hidden"}