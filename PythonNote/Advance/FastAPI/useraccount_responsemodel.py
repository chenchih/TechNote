from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()
#using data model
class RegIn(BaseModel):
    username: str
    password: str
    email: str
#hidden not showen password
class Regout(BaseModel):
    username: str
    email: str

    
#case1 hide password
@app.post("/register", response_model=RegIn) #show all data
#@app.post("/register", response_model=Regout) #show only user and email
def register(user: RegIn):
    return user

# case2 hashpassword
@app.post("/registerhash", response_model=RegIn)
def registerhash(user: RegIn):
    user.password= hashlib.sha1(user.password.encode('utf-8')).hexdigest()
    return user

#run request post command:
#import request 
#import json
#requests.post(url='http://127.0.0.1:8000/register', data=json.dumps({'username': 'hellotest', 'password': '123456','email': 'hello@test.com'})).text
# curl -X POST -H "Content-Type: application/json" -d '{"username": "hellotest", "password": "123456", "email": "hello@test.com"}' "http://127.0.0.1:8000/register"


#case3 post and get endpoint store in dictioanry 
# POST endpoint to register a new user


# Temporary in-memory storage for demonstration
users_db = {}


@app.post("/registerNew", response_model=Regout)
def register(user: RegIn):
    # Store the user in a dictionary
    users_db[user.username] = user
    return user
    
# GET endpoint to retrieve user data by username
@app.get("/registerNew/{username}", response_model=RegIn)
def get_user(username: str):
    user = users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user