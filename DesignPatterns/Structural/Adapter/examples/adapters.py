from example_service import UserService, DatabaseUserRepository, ExternalAPIUserService, Dict
# Adapter for Database
class DatabaseUserAdapter(UserService):
    def __init__(self, database_repo: DatabaseUserRepository):
        self._adaptee = database_repo
    
    def get_user(self, username: str) -> Dict:
        # Adapt the database response to our expected format
        db_user = self._adaptee.fetch_by_username(username)
        return {
            "username": db_user["user_id"],
            "fname": db_user["first"],
            "lname": db_user["last"],
            "gender": "Male" if db_user["sex"] == "M" else "Female",
            "age": db_user["years"]
        }
    
    def create_user(self, user_data: Dict) -> bool:
        # Adapt our format to database format
        db_format = {
            "user_id": user_data["username"],
            "first": user_data["fname"],
            "last": user_data["lname"],
            "sex": user_data["gender"][0].upper(),  # M/F
            "years": user_data["age"]
        }
        return self._adaptee.insert_user_record(db_format)

# Adapter for External API
class APIUserAdapter(UserService):
    def __init__(self, api_service: ExternalAPIUserService):
        self._adaptee = api_service
    
    def get_user(self, username: str) -> Dict:
        api_user = self._adaptee.retrieve_user(username)
        return {
            "username": api_user["login"],
            "fname": api_user["given_name"],
            "lname": api_user["family_name"],
            "gender": api_user["gender"],
            "age": api_user["age"]
        }
    
    def create_user(self, user_data: Dict) -> bool:
        api_format = {
            "login": user_data["username"],
            "given_name": user_data["fname"],
            "family_name": user_data["lname"],
            "gender": user_data["gender"],
            "age": user_data["age"]
        }
        response = self._adaptee.post_user(api_format)
        return response["status"] == "success"
    

# Client code works with the UserService interface consistently
def display_user(service: UserService, username: str):
    user = service.get_user(username)
    print(f"{user['fname']} {user['lname']} ({user['gender']}, {user['age']})")

# Using the Database Adapter
db_repo = DatabaseUserRepository()
db_adapter = DatabaseUserAdapter(db_repo)
display_user(db_adapter, "johndoe")

# Using the API Adapter
api_service = ExternalAPIUserService()
api_adapter = APIUserAdapter(api_service)
display_user(api_adapter, "janesmith")

# Both adapters work with the same interface
services = [db_adapter, api_adapter]
for service in services:
    service.create_user({
        "username": "newuser",
        "fname": "Alice",
        "lname": "Wonderland",
        "gender": "Female",
        "age": 28
    })