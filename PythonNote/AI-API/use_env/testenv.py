import os
from dotenv import load_dotenv

# Load values from .env into environment variables
load_dotenv()

# Now you can get them anywhere in your app
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")

print("Database user:", db_user)
print("Database password:", db_pass)  # don't do this in real apps 😅
print("Database name:", db_name)

# Example: Build a database connection string
connection_url = f"postgresql://{db_user}:{db_pass}@localhost:5432/{db_name}"
print("Connection URL:", connection_url)