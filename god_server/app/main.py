from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from app.utils import generate_key
from app.database import get_db, create_clock_task, get_clock_task

app = FastAPI()

class KeyRequest(BaseModel):
    application_use: str
    company_name: str

class ClockRequest(BaseModel):
    encrypted_data: str

class DeclockRequest(BaseModel):
    clock_task_id: str

@app.post("/api/generate_keys")
def generate_keys(request: KeyRequest):
    application_key = generate_key()
    company_key = generate_key()
    return {
        "application_key": application_key,
        "company_key": company_key
    }

@app.post("/api/clock")
def clock_data(request: ClockRequest, db=Depends(get_db)):
    clock_task_id = create_clock_task(db, request.encrypted_data)
    return {"clock_task_id": clock_task_id}

@app.post("/api/declock")
def declock_data(request: DeclockRequest, db=Depends(get_db)):
    encrypted_data = get_clock_task(db, request.clock_task_id)
    if encrypted_data is None:
        raise HTTPException(status_code=404, detail="Clock task ID not found")
    return {"encrypted_data": encrypted_data}
