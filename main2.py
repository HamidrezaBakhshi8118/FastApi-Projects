from fastapi import FastAPI  , Query , status , HTTPException , Path , Form  , Body , UploadFile , File , Depends 
from fastapi.responses import JSONResponse 
from typing import Annotated
import random
from typing import List
from schemas import PersonCreateSchema , PersonResponseSchema , CreatUser , AccountCreatRequest
from DataBase import User , Addres , SessionLocal
from sqlalchemy.orm import Session
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
import bcrypt


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app=FastAPI()
security = HTTPBasic()

def hash_password(password: str) -> str:
    # تبدیل پسورد متنی به bytes
    pwd_bytes = password.encode('utf-8')
    # تولید salt و هش کردن
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    # بازگرداندن به صورت string برای ذخیره در دیتابیس
    return hashed.decode('utf-8')


@app.get("/names" , response_model=list[PersonResponseSchema])
def get_names(q : str | None = Query(alias="search",default=None , max_length=50),db : Session = Depends(get_db)):
    query = db.query(User)
    if q :
        query=query.where(User.first_name.like(f"%{q}%"))
        result=query.all()
        if result:    
            return result
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="object not found")


@app.post("/AddPerson",status_code=status.HTTP_201_CREATED)
def creat_user(user : CreatUser = Form(),db : Session = Depends(get_db)):
    if user:
        new_user=User(first_name=user.first_name, last_name=user.last_name , age = user.age)
        db.add(new_user)
        db.commit()
        return user
    
@app.get("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    return {
        "username": credentials.username,
        "password": credentials.password
    }

@app.post("/creat_account")
def creat_account(account : AccountCreatRequest = Form() , db : Session = Depends(get_db)):
    existing_user = db.query(User).where(User.username == account.username).first()
    if existing_user :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST , detail="Username already exists")
    
    new_user = User(first_name = account.first_name ,
                    last_name = account.last_name ,
                    age = account.age ,
                    username = account.username , 
                    password = hash_password(account.password)
                    )

    db.add(new_user)
    db.commit()

    return account