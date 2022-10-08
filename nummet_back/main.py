from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from endpoints import SLAERouter, DeterminantRouter, InverseRouter

app = FastAPI(title="Nummet API")


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(SLAERouter.router, prefix="/slae", tags=["slae"])
app.include_router(DeterminantRouter.router, prefix="/det", tags=["det"])
app.include_router(InverseRouter.router, prefix="/inv", tags=["inv"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, host="0.0.0.0", reload=True)