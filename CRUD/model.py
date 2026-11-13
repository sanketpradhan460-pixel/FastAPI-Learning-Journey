from pydantic import BaseModel

class employee(BaseModel):
    id:int
    name:str
    dept:str
    age:int