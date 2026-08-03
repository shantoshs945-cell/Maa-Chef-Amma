from fastapi import APIRouter
from database import supabase
from pydantic import BaseModel
from typing import Optional, Any

router = APIRouter()

class Product(BaseModel):
    name: str
    description: Optional[str] = ""
    category: str
    price: int
    mrp: Optional[int] = None
    weight: Optional[str] = ""
    spice: Optional[str] = ""
    icon: Optional[str] = "ti-drumstick"
    badge: Optional[str] = ""
    badge_text: Optional[str] = ""
    rating: Optional[float] = 4.5
    review_count: Optional[int] = 0
    is_active: Optional[bool] = True
    image_url: Optional[str] = None
    ingredients: Optional[str] = ""
    how_to_use: Optional[str] = ""
    storage_info: Optional[str] = ""
    variants: Optional[Any] = None

@router.get("/")
def get_products():
    res = supabase.table("products").select("*").eq("is_active", True).execute()
    return res.data

@router.post("/")
def add_product(p: Product):
    res = supabase.table("products").insert(p.dict()).execute()
    return res.data

@router.put("/{id}")
def update_product(id: int, p: Product):
    res = supabase.table("products").update(p.dict()).eq("id", id).execute()
    return res.data

@router.delete("/{id}")
def delete_product(id: int):
    res = supabase.table("products").update({"is_active": False}).eq("id", id).execute()
    return {"message": "Product hidden"}