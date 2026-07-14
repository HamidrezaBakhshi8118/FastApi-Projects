from pydantic import BaseModel ,EmailStr


class PersonCreateSchema(BaseModel):
    name : str


class PersonResponseSchema(BaseModel):
    id : int
    name : str

class PersonUpdateSchema(BaseModel):
    name : str 



class User(BaseModel):
    name: str
    email:EmailStr
    account_id : int

    