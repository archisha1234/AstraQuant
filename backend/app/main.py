from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import optimize, quantum

app = FastAPI(title="AstraQuant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# root test
@app.get("/")
def root():
    return {"status": "AstraQuant backend running 🚀"}

# include routes
app.include_router(optimize.router)
app.include_router(quantum.router)

print(optimize)