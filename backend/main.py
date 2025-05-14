# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

app = FastAPI()

# Permitir peticiones desde HTML
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

client = MongoClient("mongodb://localhost:27017/")
db = client["clinica_db"]

@app.get("/hola")
def hola_mundo():
    db.saludos.insert_one({"mensaje": "Hola desde MongoDB!"})
    return {"mensaje": "Hola Mundo desde el backend FastAPI!"}
