from base_class import User
from concrete_user_classes import AdminUser, RegularUser

class UserFactory:
    def __init__(self):
        self._creators = {}

    def register_user_type(self, role: str, creator):
        self._creators[role] = creator

    def create_user(self, role: str, username: str) -> User:
        if not username or len(username.strip()) < 3:
            raise ValueError("Username must be at least 3 characters.")
        
        creator = self._creators.get(role.lower())
        if not creator:
            raise ValueError(f"User type '{role}' is not registered.")
        
        return creator(username)

if __name__ == "__main__":
    # Initialize the factory
    factory = UserFactory()

    # Register types
    factory.register_user_type("admin", AdminUser)
    factory.register_user_type("regular", RegularUser)

    # Create user objects
    admin = factory.create_user("admin", "admin_kib")
    regular = factory.create_user("regular", "john_doe")

    print(f"{admin.username} created with role: {admin.get_role()}")
    print(f"{regular.username} created with role: {regular.get_role()}")
