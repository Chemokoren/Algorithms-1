import base64
import json
import time
from base_class import User

def generate_token(user: User) -> str:
    payload = {
        "id": user.id,
        "username": user.username,
        "role": user.get_role(),
        "iat": int(time.time())
    }
    token = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()
    return token
