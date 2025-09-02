# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import create_tables

# import routers
from api.routers import tables, orders, menu

# create FastAPI app
app = FastAPI(title="Easy Order API")
create_tables()

# ------------------- CORS -------------------
# allow frontend running from any origin to access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------- Routers -------------------
app.include_router(tables.router)
app.include_router(orders.router)
app.include_router(menu.router)

# ------------------- Root Endpoint -------------------
@app.get("/")
def root():
    return {"message": "Easy Order API is running!"}