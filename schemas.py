from pydantic import BaseModel ,EmailStr , Field


class PersonCreateSchema(BaseModel):
    name : str


class PersonResponseSchema(BaseModel):
    id: int
    first_name: str
    last_name: str

class PersonUpdateSchema(BaseModel):
    name : str 



class User(BaseModel):
    name: str
    email:EmailStr
    account_id : int


class CreatUser(BaseModel):
    first_name : str = Field(... , min_length=3)
    last_name : str = Field(... , min_length=5)
    age : int =Field(...)
