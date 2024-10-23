from pymongo import MongoClient

from src.logai.log_store.base import BaseLogger


class MongoLogger(BaseLogger):
    def __init__(self, db_uri, db_name, log_level="INFO"):
        # super().__init__(log_level)
        self.client = MongoClient(db_uri)
        self.db = self.client[db_name]
        self.collection = self.db['logs']
        print("MongoDB connection established.")

    def create_log(self, log_entry):
        """
        Store a log entry in MongoDB.

        Parameters:
            log_entry (dict): The log entry containing 'timestamp', 'level', 'message', 'module', and 'metadata'.
        """
        self.collection.insert_one(log_entry)
        print(f"Log entry added to MongoDB: {log_entry['message']}")

    def close_connection(self):
        """Close the MongoDB connection."""
        self.client.close()
        print("MongoDB connection closed.")
