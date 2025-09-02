# api/routers/orders.py
from fastapi import APIRouter, HTTPException
from typing import List
import json

from api.schemas import OrderCreate, OrderUpdate, OrderOut, OrderItem
from database import get_orders, add_order, update_order_status

router = APIRouter(prefix="/orders", tags=["orders"])

def _rows_to_orders(rows) -> List[OrderOut]:
    """Convert database rows into OrderOut objects."""
    orders = []
    for r in rows:
        items_list = json.loads(r[2])
        items = [OrderItem(**i) for i in items_list]
        orders.append(OrderOut(id=r[0], table_number=r[1], items=items, status=r[3]))
    return orders

@router.get("", response_model=List[OrderOut])
def list_orders():
    rows = get_orders()
    return _rows_to_orders(rows)

@router.post("", response_model=OrderOut, status_code=201)
def create_order(payload: OrderCreate):
    order_id = add_order(payload.table_number, payload.items, payload.status)
    return OrderOut(id=order_id, table_number=payload.table_number, items=payload.items, status=payload.status)

@router.patch("/{order_id}", response_model=OrderOut)
def patch_order(order_id: int, payload: OrderUpdate):
    orders = get_orders()
    order_ids = {r[0] for r in orders}
    if order_id not in order_ids:
        raise HTTPException(status_code=404, detail="Order not found.")
    update_order_status(order_id, payload.status)
    order_row = next(r for r in orders if r[0] == order_id)
    items_list = json.loads(order_row[2])
    items = [OrderItem(**i) for i in items_list]
    return OrderOut(id=order_id, table_number=order_row[1], items=items, status=payload.status)

@router.delete("/{order_id}", status_code=204)
def delete_order_route(order_id: int):
    orders = get_orders()
    order_ids = {r[0] for r in orders}
    if order_id not in order_ids:
        raise HTTPException(status_code=404, detail="Order not found.")
    delete_order(order_id)
    return