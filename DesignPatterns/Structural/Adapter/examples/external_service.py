from user import User
"""
When to Use the Adapter Pattern
- You need to integrate with external systems that expect data in a different shape
- You want to avoid modifying your core User model
- You want to standardize formatting or conversion logic

External system expects

{
  "full_name": "John Doe",
  "user_id": "john_doe",
  "sex": "Male",
  "age_group": "Adult"
}

"""
# Adapter Pattern Implementation

# 1. Target Interface -What the client expects
class ExternalUserProfile:

    def get_profile(self)->dict:
        raise NotImplementedError
    
# Adapter Class
class UserAdapter(ExternalUserProfile):

    def __init__(self, user: User):
        self.user =user

    def get_profile(self) -> dict:
        return {
            "user_id" : self.user.username,
            "full_name": f"{self.user.fname} {self.user.lname}",
            "sex": "Male" if self.user.gender == "M" else "Female",
            "age_group": self._get_age_group(self.user.age)
        }
    
    def _get_age_group(self, age):
        if age < 18:
            return "Minor"
        elif age < 65:
            return "Adult"
        else:
            return "Senior"

user =User("jdoe", "John", "Doe", "M", 32)
adapter =UserAdapter(user)

external_payload =adapter.get_profile()
print(external_payload)
