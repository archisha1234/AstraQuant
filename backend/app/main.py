from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://your-frontend.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # KEEP WILDCARD FOR NOW (DEBUG MODE)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)