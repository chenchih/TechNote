# Create a easy FastAPI

In this note I will share on how to create a easy api for testing, using FastAPI. You need to install some libary before get to start

## Library

> Install fastapi: `pip install fastapi`

> Install server: `pip install uvicorn`

Import module: `from fastapi import fastAPI`

## Create server and the path parameter

The syntax if using fastapi is using `app=FastAPI()` , so inital it will look like this:

```
from fastapi import FastAPI

app= FastAPI()

```

### Add Path Parameter

Let add the path parameter to it

```
from fastapi import FastAPI

app= FastAPI()
items= []

#create a path in fastapi

#root
@app.get("/")
def root():
    return {"hello":"world"}

```

### Run Server

Let run the server with below command, and it will run on terminal

```
uvicorn main:app –reload
```

You can access to the URL: `http://127.0.0.1:8000/`

### Create Route

continue from above code, let create new method to add items to list.

```
.....
@app.get("/")
.....

@app.post("/items")
def create_item(item: str):
    str.append(item)
    return item
```

Now you can add items into list by send request to items need to use this command, need to open new terminal and run below:

```
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
```

In this case I am adding apple into list

## Update

- 2024.09.09: itial create (not done yet)
