# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from generate_keys import generate_keys

app = FastAPI()

class UserData(BaseModel):
    name: str
    age: str
    color: str
    email: str

@app.post("/generate-mask-keys-for-user")
def generate_mask_keys(user_data: UserData):
    keys = generate_keys()
    return keys
