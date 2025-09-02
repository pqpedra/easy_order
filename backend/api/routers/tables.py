# api/routers/tables.py
from fastapi import APIRouter, HTTPException
from typing import List
import sqlite3

from api.schemas import TableCreate, TableUpdate, TableOut
from database import get_tables, add_table, update_table_status, clear_one_table


router = APIRouter(prefix="/tables", tags=["tables"])

def _rows_to_tables(rows) -> List[TableOut]:
    """Convert database rows into TableOut objects."""
    return [TableOut(number=r[0], status=r[1]) for r in rows]

@router.get("", response_model=List[TableOut])
def list_tables():
    tables = get_tables()
    return _rows_to_tables(tables)

@router.post("", response_model=TableOut, status_code=201)
def create_table(payload: TableCreate):
    try:
        add_table(payload.number, payload.status)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Table number already exists.")
    return TableOut(number=payload.number, status=payload.status)

@router.patch("/{number}", response_model=TableOut)
def patch_table(number: int, payload: TableUpdate):
    numbers = {n for (n, s) in get_tables()}
    if number not in numbers:
        raise HTTPException(status_code=404, detail="Table not found.")
    update_table_status(number, payload.status)
    return TableOut(number=number, status=payload.status)

@router.delete("/{number}", status_code=204)
def delete_table_route(number: int):
    numbers = {n for (n, s) in get_tables()}
    if number not in numbers:
        raise HTTPException(status_code=404, detail="Table not found.")
    clear_one_table(number)
    return