from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.optimize import router as optimize_router
from app.routes.quantum import router as quantum_router

app = FastAPI(title="AstraQuant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "AstraQuant backend running 🚀"}

app.include_router(optimize_router)
app.include_router(quantum_router)