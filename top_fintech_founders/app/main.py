# app/main.py
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Top Fintech Founders API")
app.include_router(router)
