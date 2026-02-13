import os 
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def dbConnection():
    try:
        client = MongoClient(os.getenv('DB_URI'))
        print("MongoDb Connected Successfully!")
        
        return client
    except Exception as e:
        print("Error connecting MongoDb", str(e))
        
client = dbConnection()
db = client['my_Db']