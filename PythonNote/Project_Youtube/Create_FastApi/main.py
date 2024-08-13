from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

    
items= [] 

#create a path in fastapi
@app.get("/")
def root():
    return {"hello":"world"}


@app.post("/items")
#def create_item(item: str):
def create_item(item: Item):
    items.append(item)
    return items

#@app.get("/items",response_model=list[Item] )
@app.get("/items")
def list_items(limit: int = 3):
    return items[0:limit] 

# @app.get("/items/{item_id}")
# def get_item(item_id: int) -> str: 
#     item= items[item_id]
#     return item


#@app.get("/items/{item_id}", response_model=Item)
@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item: 
    if item_id< len(items):
        return items[item_id]
    else:
        raise HTTPException (status_code=404, detail= f"Item {item_id}  not found")
    