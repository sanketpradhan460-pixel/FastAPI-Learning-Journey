from fastapi import FastAPI
from pydantic import BaseModel

# 1. Define the data model
class User(BaseModel):
    id: int
    name: str

# 2. Create FastAPI application
app = FastAPI()

# 3. Define API endpoint
@app.get("/user", response_model=User)
def get_user():
    return User(id=1, name="sanket")