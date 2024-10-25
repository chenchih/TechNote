from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()

class RegIn(BaseModel):
    username: str
    password: str
    email: str
#hidden not showen password
class Regout(BaseModel):
    username: str
    email: str
 
#hide password
 
#@app.post("/register", response_model=RegIn) #show all data
@app.post("/register", response_model=Regout) #show only user and email
def register(user: RegIn):
    return user

# hashpassword
@app.post("/registerhash", response_model=RegIn)
def registerhash(user: RegIn):
    user.password= hashlib.sha1(user.password.encode('utf-8')).hexdigest()
    return user

#run request post command:
#import request 
#import json
#requests.post(url='http://127.0.0.1:8000/register', data=json.dumps({'username': 'hellotest', 'password': '123456','email': 'hello@test.com'})).text


