from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()
#Using Path parameter:



#case1: get userid with index 
@app.get("/users/{user_id}")
def get_users(user_id: int, qry: str = None):
    return {"user_id": user_id, "query": qry }


#case2 post and get request
usernames = []
@app.post("/account") #show only user and email
def create_user(user):
    usernames.append(user)
    return usernames
#["anna"]

#command: 
#curl -X POST 'http://127.0.0.1:8000/account?user=anna'
#or 
# curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/account?user=mary'

@app.get("/account/{userid}") 
def get_user(userid: int):
    username= usernames[userid]
    return username
     
#
#curl -X GET http://127.0.0.1:8000/account/0
#"mary"

# case3 using limit to display result
@app.get("/account") 
def list_userss(limit: int = 10):
    return usernames[0: limit]
# get fitst two index 
#curl -X GET http://127.0.0.1:8000/account?limit=2
# get default limit value
#curl -X GET http://127.0.0.1:8000/account


#using data model
'''
class RegIn(BaseModel):
    username: str
    password: str
    email: str
#hidden not showen password
class Regout(BaseModel):
    username: str
    email: str
 '''

'''
    
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

'''
