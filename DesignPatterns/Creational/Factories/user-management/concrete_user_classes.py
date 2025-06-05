from base_class import User

class AdminUser(User):
    def get_role(self) -> str:
        return "Admin"

class RegularUser(User):
    def get_role(self) -> str:
        return "Regular"
