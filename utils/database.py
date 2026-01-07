from pymongo import MongoClient
import os
from dotenv import load_dotenv
from utils.logs import *
from typing import Dict, Any, List

from core.loan_scheme import LoanScheme

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

    def insert_into_collection(self, collection_name : str, data: Dict[str, Any]):
        try:
            collection = self._db[collection_name]
            result = collection.insert_one(data)
            return result.inserted_id
        except:
            log_error(f"Couldn't insert data into collection {collection_name}!")
            return None

    def fetch_all_from_collection(self, collection_name : str) -> List[Dict[str, Any]]:
        try:
            collection = self._db[collection_name]

            # .find({}) retrieves all documents; we cast the cursor to a list
            schemes = list(collection.find({}))
            
            return schemes
        except:
            log_error(f"Couldn't retrieve data from collection {collection_name}!")
            return None
    
    def insert_loan_scheme(self, loan_scheme : LoanScheme):
        dump = loan_scheme.model_dump()
        self.insert_into_collection("loan_schemes", dump)
        
    def fetch_all_loan_schemes(self):
        d_list = self.fetch_all_from_collection("loan_schemes")
        loan_schemes = []
        for d in d_list:
            loan_scheme = LoanScheme(**d)
            loan_schemes.append(loan_scheme)
        return loan_schemes
    
db = Database()

def get_db():
    return db.db

def get_db_wrapper():
    return db
