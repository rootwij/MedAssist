from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(title="MedAssist: Healthcare Assistant")

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Welcome to MedAssist!"}
