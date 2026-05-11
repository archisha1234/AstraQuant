from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AstraQuant API")

# CORS (safe for frontend + production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://your-frontend.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ ROOT ENDPOINT (VERY IMPORTANT FOR TESTING)
@app.get("/")
def root():
    return {
        "status": "AstraQuant backend is running 🚀",
        "docs": "/docs"
    }

# OPTIONAL TEST ENDPOINT
@app.get("/health")
def health():
    return {"status": "ok"}