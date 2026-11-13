from pydantic import BaseModel,Field,StrictInt
from typing import Optional

class employee(BaseModel): 
    # ... -> id is required
    #  gt -> greater than equal to 
    id:int =Field(...,gt=0)
    name:str =Field(...,min_length=6,max_length=10)
    dept:str=Field(...,min_length=3,max_length=10)
    # using StrictInt only takes takes the value when int 
    # age gets optional , if user does give any thing values gets none
    age:Optional[StrictInt]=Field(default=None)

