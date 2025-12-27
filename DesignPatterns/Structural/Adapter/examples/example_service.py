"""
The Adapter Design Pattern helps make incompatible interfaces work together.
In the context of managing User Table:-
a) Adapt different data sources (CSV, API, Database) to a common interface
b) Handle legacy systems with different field names
c) Provide a unified interface for user operations
"""
# target interface - what your application expects
from abc import ABC, abstractmethod
from typing import Dict

class UserService(ABC):
    """Target Interface that user application expects"""

    @abstractmethod
    def get_user(self, username: str)->Dict:
        pass

    @abstractmethod
    def create_user(self, user_data:Dict)->bool:
        pass

    @abstractmethod
    def update_user(self, username:str, update_user:Dict)->bool:
        pass

# Create the Adaptee - Existing implementations that need adapting
# Database User Repository (Adaptee)
class DatabaseUserRepository:
    """Legacy database implementation with different method names"""
    def fetch_by_username(self, user_id:str):
        # Actual database query
        return {"user_id":user_id,"first":"John", "last":"Doe", "sex":"M", "years":30}
    
    def insert_user_record(self, record: dict):
        print("Inserting to database: {record}")
        return True
    
# API User Service (Adaptee)
class ExternalAPIUserService:
    """External API with different field names"""
    def retrieve_user(self, user_identifier: str):
        # API call
        return {"login": user_identifier, "given_name": "Jane", "family_name": "Smith", "gender": "F", "age": 25}
    
    def post_user(self, payload: dict):
        print(f"Posting to API: {payload}")
        return {"status": "success"}
    
