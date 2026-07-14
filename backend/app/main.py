from fastapi import FastAPI

app = FastAPI(
    title="AI Study Assistant API",
    version="1.0.0",
    description="Backend API for an AI-powered Study Assistant."
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Study Assistant!"
    }

@app.get("/health")
def health():
    return {
        "status": "Server is running",
        "version": "1.0.0"
    }
