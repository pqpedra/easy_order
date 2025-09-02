# api/routers/menu.py
from fastapi import APIRouter, HTTPException
from typing import List
from database import add_menu_item, get_menu, delete_menu_item
from api.schemas import MenuItemCreate, MenuItemOut

router = APIRouter(prefix="/menu", tags=["menu"])

@router.get("", response_model=List[MenuItemOut])
def list_menu():
    items = get_menu()
    return [MenuItemOut(id=i[0], name=i[1], category=i[2], price=i[3]) for i in items]

@router.post("", response_model=MenuItemOut, status_code=201)
def create_menu_item(payload: MenuItemCreate):
    add_menu_item(payload.name, payload.category, payload.price)
    items = get_menu()
    # return the last inserted item
    last_item = items[-1]
    return MenuItemOut(id=last_item[0], name=last_item[1], category=last_item[2], price=last_item[3])

@router.delete("/{item_id}", status_code=204)
def delete_menu_item_route(item_id: int):
    items = get_menu()
    ids = [i[0] for i in items]
    if item_id not in ids:
        raise HTTPException(status_code=404, detail="Menu item not found")
    delete_menu_item(item_id)
    return