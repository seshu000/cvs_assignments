from fastapi import FastAPI, Request
from sqlalchemy import create_engine, text
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI()

SCHEMA = ["name", "age"]


def get_db():
    dir1 = os.path.dirname(__file__)
    DATABASE = os.path.join(dir1, "people.db")
    db = create_engine("sqlite:///" + DATABASE)
    return db 
    
def get_all():
    eng = get_db()
    with eng.connect() as conn:
        res = conn.execute(text("select name, age from people")).fetchall()
    return [dict(zip(SCHEMA,row)) for row in res]

def get_age(name:str):
    eng = get_db()
    with eng.connect() as conn:
        result=conn.execute(
        text("select age from people where name = :name"),
        {"name":name}
        ).fetchone()
        if result:
            return result[0]
        else:
            raise NotFound()


class Createdata(BaseModel):
    name:str
    format:str
    
@app.get("/all")
def api_getall():
    return get_all()
    

@app.get("/helloj/{name}/{format}")
async def helloj_path(name: str, format: str):
    return {"name": name, "format": format}

@app.post("/helloj")
async def helloj_post(Request:Createdata):
    return _helloj(Request.name, Request.format)
   
def _helloj(fname:str,fformat:str):
    try:
        age=get_age(fname)
        return JSONResponse(content={"name":fname,"age":age},status_code=200)
    except:
        return JSONResponse(content={"name":fname,"details":"Not Found"},status_code=500)
        
        

