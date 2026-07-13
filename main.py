from fastapi import FastAPI  , Query , status , HTTPException , Path , Form  , Body , UploadFile , File
from fastapi.responses import JSONResponse
from typing import Annotated
import random
from typing import List
from schemas import PersonCreateSchema , PersonResponseSchema

app=FastAPI()


names=[
    {"id":1,"name":"ali"},
    {"id":2,"name":"ahmad"},
    {"id":3,"name":"hossein"},
    {"id":4,"name":"reza"},
    {"id":5,"name":"mohsen"},
]


@app.get("/names" , response_model=list[PersonResponseSchema])
def get_names(q : str | None = Query(alias="search",default=None , max_length=50)):
    if q :
        return JSONResponse(content=[item for item in names if item['name'] == q ])
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="object not found")


@app.get("/names/{name_id}",response_model=PersonResponseSchema)
def get_name_by_id(name_id:int = Path(title="object id")):
    for name in names:
        if name['id'] == name_id:
            return name
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="object not found")


@app.post("/names",status_code=status.HTTP_201_CREATED)
def creat_name(name : str = Body(embed=True)):
    name_obj={"id":random.randint(6,100),"name":name}
    names.append(name_obj)
    return name_obj


@app.put("/names/{name_id}" )
def update_name(name_id:int = Path(),name:str=Query()):
    for item in names:
        if item['id']==name_id:
            item['name'] = name
            return name
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="object not found")


@app.delete("/names/{name_id}")
def delete_name(name_id:int):
    for item in names:
        if item['id'] == name_id:
            names.remove(item)
            return {"message":"item deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="object not found")    


@app.get("/")
def root():
    return JSONResponse(content={"message":"server testing"},status_code=status.HTTP_202_ACCEPTED)

@app.post("/submit")
def submit_form(username :str = Form(... , alias="username"), password:str=Form(... , alias="password")):
    return {"username": username, "password": password}


@app.post("/uploadfile")
async def upload_file(file : UploadFile = File(...)):
    content = await file.read()
    print(file.__dict__)
    return {"filename" : file.filename , "content_type":file.content_type , "file_size": len(content)}


@app.post("/UploadMultipleFiles")
async def upload_multiple(files: List[UploadFile] = File(description="Select files to upload")):
    
    return [
        {"filename": file.filename, "content_type": file.content_type} 
        for file in files
    ]


@app.post("/namesSchema",status_code=status.HTTP_201_CREATED,response_model=PersonResponseSchema)
def creat_name(person : PersonCreateSchema):
    name_obj={"id":random.randint(6,100),"name":person.name}
    names.append(name_obj)
    return name_obj