from fastapi import FastAPI
from backend.routes.chat import router as chat_router

app = FastAPI(title="Jarvis Odoo Agent")

app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "Jarvis Odoo Agent Running"}
