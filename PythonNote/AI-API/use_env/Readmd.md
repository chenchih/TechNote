# How to proected your API or password key

In this example I would like to show you an exmaplel of using `.env` file to protected your secure your account like api key, or pawword. 

Placing your Key in .env is the safest way to secure privacy,python code will read `.env` file and get the password 


## How to use?

- `.env` file:
```
DB_USER="test"
DB_PASS=mypassword123
DB_NAME=mydatabase
```

- python script: 
```
import os
from dotenv import load_dotenv

# Load values from .env into environment variables
load_dotenv()

# Now you can get them anywhere in your app
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")
```

