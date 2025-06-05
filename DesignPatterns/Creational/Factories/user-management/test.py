from factory_method import UserFactory

if __name__ == "__main__":
    user1 = UserFactory.create_user("admin", "alice")
    user2 = UserFactory.create_user("regular", "bob")

    print(f"{user1.username} is an {user1.get_role()}")
    print(f"{user2.username} is a {user2.get_role()}")
