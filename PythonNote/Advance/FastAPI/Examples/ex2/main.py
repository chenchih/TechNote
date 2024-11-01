#reference: https://www.youtube.com/watch?v=65D-1FSGUt0&t=611s
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional, List, Set, Union



app= FastAPI()

users= {
#"x": {'id':0},
"a": {'id':1, 'username':'a'},
"b": {'id':2, 'username':'b', 'username':'bbb'},
"c": {'id':3, 'username':'c', 'username':'ccc', 'description':'default'},
"d": {'id':4, 'username':'d', 'username':'ddd', 'description':'user d'},
"e": {'id':5, 'username':'e', 'username':'eee', 'description':'user e', 'gender':'F'},
}

#Define Model for Structure
class UserOut(BaseModel):
    id: int
    username: str
    description: Optional[str]= 'default' #if not contain description will display default



#using it in the endpoint

#response_model_include={"id"} #will only output id
#response_model_exclude={"id", "username"} # not display id and username
#response_model_exclude_unset=True #compare value and return value, no match not display output

@app.get('/users/{username}', response_model=UserOut)
async def get_user(username: str):
    if username is None:
        raise HTTPException(status_code=404, detail="User not found")
    return users.get(username, {})




#get all data in list 
@app.get('/users', response_model=List[UserOut])
async def get_users():
    return users.values()

   
if __name__=='__main__':

    uvicorn.run("main:app", reload=True)
#if request not contain key in value then will ocuur interal error
# you can use the optional to avoid interal error 
# in  x key, we don;t have username, but you send request with a then error occur
# in a key we don't have description but description is been set optional and set a default value, which wil use default as value 
 
    
