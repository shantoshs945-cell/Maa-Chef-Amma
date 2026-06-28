from fastapi import APIRouter
from database import supabase
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class Category(BaseModel):
    name: str
    slug: str
    color: Optional[str] = '#B5451B'
    bg_color: Optional[str] = '#FAECE7'

@router.get("/")
def get_categories():
    res = supabase.table("categories").select("*").order("name").execute()
    return res.data

@router.post("/")
def add_category(c: Category):
    res = supabase.table("categories").insert(c.dict()).execute()
    return res.data

@router.put("/{id}")
def update_category(id: int, c: Category):
    res = supabase.table("categories").update(c.dict()).eq("id", id).execute()
    return res.data

@router.delete("/{id}")
def delete_category(id: int):
    res = supabase.table("categories").delete().eq("id", id).execute()
    return {"message": "Category deleted"}