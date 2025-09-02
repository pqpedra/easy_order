# api/schemas.py
from pydantic import BaseModel
from typing import List

# --- TABLE SCHEMAS ---
class TableCreate(BaseModel):
    number: int
    status: str = "available"

class TableUpdate(BaseModel):
    status: str

class TableOut(BaseModel):
    number: int
    status: str


# --- ORDER SCHEMAS ---
class OrderItem(BaseModel):
    item: str
    quantity: int

class OrderCreate(BaseModel):
    table_number: int
    items: List[OrderItem]
    status: str = "pending"

class OrderUpdate(BaseModel):
    status: str

class OrderOut(BaseModel):
    id: int
    table_number: int
    items: List[OrderItem]
    status: str


# --- MENU SCHEMAS ---
class MenuItemCreate(BaseModel):
    name: str
    category: str
    price: float

class MenuItemOut(BaseModel):
    id: int
    name: str
    category: str
    price: float