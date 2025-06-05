from base_class import User
from concrete_user_classes import AdminUser, RegularUser
from generate_token import generate_token
class UserFactory:
    @staticmethod
    def create_user(user_type: str, username: str) -> User:
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters long.")
        
        if user_type == "admin":
            user=AdminUser(username)
        
        elif user_type == "regular":
            user=RegularUser(username)
        else:
            raise ValueError(f"Unknown user type: {user_type}")
        
        user.save()
        return user

if __name__ == "__main__":
    user1 = UserFactory.create_user("admin", "alice")
    user2 = UserFactory.create_user("regular", "bob")

    print(f"{user1.username} is an {user1.get_role()}, Token: {generate_token(user1)}")
    print(f"{user2.username} is a {user2.get_role()}, Token: {generate_token(user1)}")