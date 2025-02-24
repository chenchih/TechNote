from fastapi import FastAPI
import random
app= FastAPI()

@app.get('/')
async def root():
    return {'example': 'This is an example', 'data':0}

@app.get('/random')
async def get_random():
        ranNum:int = random.randint(0,1000)
        return {'numbers': ranNum, 'limit': 1000 }

@app.get('/random/{limit}')
async def get_random(limit :int):
    ranNum:int = random.randint(0,limit)
    return {'numbers': ranNum, 'limit': limit }