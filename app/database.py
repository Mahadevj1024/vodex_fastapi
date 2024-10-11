from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')  # For local instance
        # For MongoDB Atlas, use: self.client = MongoClient("your_atlas_connection_string")
        self.db = self.client['fastapi_assignment']

    def get_items_collection(self):
        return self.db.items

    def get_clock_in_collection(self):
        return self.db.clock_in_records
