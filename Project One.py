from pymongo import MongoClient 
from bson.objectid import ObjectId 
from urllib.parse import quote_plus

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Connection Variables 
        print(f"Connecting with user: {username} and pass: {password}")
        USER = quote_plus(username) 
        PASS = quote_plus(password) 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/?authSource=admin') 
        self.database = self.client[DB] 
        self.collection = self.database[COL] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        """
        Inserts a document into the specified MongoDB database and collection.
        """
        if data is not None and isinstance(data, dict):
            try:
                insert_result = self.collection.insert_one(data)
                #Check if the document was inserted successfully
                if insert_result.acknowledged:
                    return True
                else:
                    return False
            except Exception as e:
                print(f"An error occured during insert: {e}")
                return False
        else:
            raise Exception("Nothing to save, due to data parameters being empty or not a dictionary")
    def read(self, query=None):
        if query is not None and isinstance(query, dict):
            try:
                #Must use find(0 rather than find_one()
                cursor = self.collection.find(query)
                #Convert the cursor to a list and return
                return list(cursor)
            except Exception as e:
                print(f"An error occured during query: {e}")
                return []
        else:
            return []
    def update (self, query, new_data):
        if query is not None and isinstance(query, dict) and new_data is not None and isinstance(new_data, dict):
            try:
                #Use update_many to modify all matching documents
                result = self.collection.update_many(query, {"$set": new_data})
                return result.modified_count
            except Exception as e:
                print(f"An error occured during update: {e}")
                return 0
        else:
            raise Exception("Update failed: Search query and new data must be non empty dictionaries")
    def delete(self, query):
        if query is not None and isinstance(query, dict):
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"An error occured during delete: {e}")
                return 0
        else:
            raise Exception("Delete failed: Search query must be a non empty dictionary")