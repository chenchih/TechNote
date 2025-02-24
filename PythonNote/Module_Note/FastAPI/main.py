from fastapi import FastAPI,HTTPException
import random 


app = FastAPI()

# root example
@app.get("/")
def root():
    return {"hello":"world"}

@app.get('/test/')
def root():
    return {'Hello': 'test'}
    
# random endpoint example
@app.get("/random")
def get_random():
    randomNumber= random.randint(0,100)
    return {"number":randomNumber, 'limit':100}
    
@app.get("/random/{limit}")
def get_random(limit: int):
    randomNumber= random.randint(0,limit)
    return {"number":randomNumber, 'limit':limit}

# items endpoint example
items = []

#create a post 
@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items
    
#get items with 
@app.get("/items")
def list_items(limit: int = 3):
    return items[0:limit]
    
# get item with Index ID
#@app.get("/items/{item_id}")
#def get_item(item_id: int) -> str:
    #item= items[item_id]
    #return item

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id< len(items):
        return items[item_id]
    else:
        raise HTTPException (status_code=404, detail= f"Item {item_id}  not found")
    
