from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
'''
items = []
#create model
class Item(BaseModel):
    id: int
    name: Optional[str] = None
    price: float
    is_active: bool = True

app = FastAPI()
#create endpoint
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    #return {"id": item_id, "name": "Foo", "price": 35.4, "is_active": True}
    return {"id": item_id, "price": 35.4, "is_active": True}
    
#POST endpoint: sends or creates new data
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items
'''
app = FastAPI()


users= {
 "x": {'id':0},
"a": {'id':1, 'username':'a'},
"b": {'id':2, 'username':'b', 'username':'bbb'},
"c": {'id':3, 'username':'c', 'username':'ccc', 'description':'default'},
"d": {'id':4, 'username':'d', 'username':'ddd', 'description':'user d'},
"e": {'id':5, 'username':'e', 'username':'eee', 'description':'user e', 'gender':'F'},
}


class UserOut(BaseModel):
    id: int
    username: str
    description: Optional[str] = 'default'
    

@app.get('/users/{username}', response_model=UserOut, response_model_include={"id", "username"})
async def get_user(username: str):
    user = users.get(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return users.get(username, {})