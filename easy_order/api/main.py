# api/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import ensure_schema
from api.routers import tables

app = FastAPI(
    title="Easy Order API",
    version="0.1.0",
    description="Simple REST API for Easy Order (tables first)."
)

# (Opcional) CORS para futuro frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajuste para domínios específicos no futuro
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    ensure_schema()

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Routers
app.include_router(tables.router)
