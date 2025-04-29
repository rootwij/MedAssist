from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router

app = FastAPI(title="MedAssist: Healthcare Assistant")

# ✅ Allow requests from frontend (Lovable app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://medassist-chat-buddy.lovable.app"],  # or ["*"] for dev/testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ API routes
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Welcome to MedAssist!"}
