from datetime import datetime
from abc import ABC, abstractmethod


class BaseLogger(ABC):
    @abstractmethod
    def create_log(self, log_entry):
        """
        Abstract method to store a log entry.
        Must be implemented by each subclass (e.g., MongoDB, PostgreSQL, SQLite).
        
        Parameters:
            log_entry (dict): The log entry containing 'timestamp', 'level', 'message', 'module', and 'metadata'.
        """
        pass
    
    
# class BaseLogger:
#     def __init__(self, log_level="INFO"):
#         self.log_level = log_level

#     def create_log(self, log_entry:dict):
        
#         self.store_log(log_entry)

#     def store_log(self, log_entry):
#         """This method will be implemented in child classes"""
#         raise NotImplementedError("This method should be implemented by subclasses")
