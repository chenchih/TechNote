from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class RegIn(BaseModel):
    username: str
    password: str
    email: str
#hidden not showen password
class Regout(BaseModel):
    username: str
    email: str
    
@app.post("/register", response_model=RegIn)
def register(user: RegIn):
    return user


#requests.post(url='hrttp://127.0.0.1:5000/register', data.json.dumps({'username': hellotest, 'password': '123456','email': 'hello@test.com' }))

