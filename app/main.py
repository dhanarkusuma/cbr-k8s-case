from fastapi import FastAPI
from app.routers.case_router import router as case_router

app = FastAPI()

app.include_router(case_router)

@app.get("/health")
def health():
    return {"status": "ok"}


