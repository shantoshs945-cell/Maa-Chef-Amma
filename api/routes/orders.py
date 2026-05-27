from fastapi import APIRouter
from database import supabase
from pydantic import BaseModel
from typing import Any

router = APIRouter()

class Order(BaseModel):
    customer_name: str
    phone: str
    address: str
    payment_method: str
    total: int
    items: Any

@router.get("/")
def get_orders():
    res = supabase.table("orders").select("*").order("created_at", desc=True).execute()
    return res.data

@router.post("/")
def place_order(o: Order):
    res = supabase.table("orders").insert(o.dict()).execute()
    return res.data

@router.put("/{id}/status")
def update_status(id: int, status: str):
    res = supabase.table("orders").update({"status": status}).eq("id", id).execute()
    return res.data