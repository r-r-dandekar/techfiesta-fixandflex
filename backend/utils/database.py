from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    _instance = None
    _client = None
    _db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._connect()
        return cls._instance
    
    def _connect(self):
        try:
            mongo_uri = os.getenv('MONGODB_URI')

            if not mongo_uri:
                raise Exception("MONGO_URI not found in env")
            
            self._client = MongoClient(mongo_uri)

            self._client.admin.command('ping')
            print("Successful")

            db_name = os.getenv('DB_NAME', 'loan_eligibility_db')
            self._db = self._client[db_name]
            
        except Exception as e:
            print("Connection failed")
            raise e
    
    @property
    def db(self):
        return self._db
    
    @property
    def client(self):
        return self._client
    
db = Database()

def get_db():
    return db.db