from pydantic import BaseModel , Field


class PersonCreateSchema(BaseModel):
    name : str


class PersonResponseSchema(BaseModel):
    id: int
    first_name: str
    last_name: str

class PersonUpdateSchema(BaseModel):
    name : str 




class CreatUser(BaseModel):
    first_name : str = Field(... , min_length=3)
    last_name : str = Field(... , min_length=5)
    age : int =Field(...)


class AccountCreatRequest(BaseModel):
    first_name : str = Field(... , min_length=3)
    last_name : str = Field(... , min_length=5)
    age : int =Field(...)
    username : str = Field(... , min_length=3 , max_length=50)
    password : str = Field(... , min_length=8 , max_length=20)

    def __repr__(self):
        return f"first_name : {self.first_name} , last_name : {self.last_name} , age : {self.age} , username : {self.username} , pass : {self.password}"
    

class Login(BaseModel):
    username : str 
    password : str


class GetAuthenticatedUser(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    age: int  

    model_config ={
        "from_attributes" : True
    }
        