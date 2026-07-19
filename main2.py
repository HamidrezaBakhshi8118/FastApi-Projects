from fastapi import FastAPI  , Query , status , HTTPException , Path , Form  , Body , UploadFile , File , Depends
from fastapi.responses import JSONResponse
from typing import Annotated
import random
from typing import List
from schemas import PersonCreateSchema , PersonResponseSchema , CreatUser
from DataBase import User , Addres , SessionLocal
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app=FastAPI()




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