import sqlite3
import uuid

from abc import ABC, abstractmethod

# Initialize DB
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    username TEXT UNIQUE,
    role TEXT
)
""")
conn.commit()

class User(ABC):
    def __init__(self, username: str):
        self.id = str(uuid.uuid4())
        self.username = username

    @abstractmethod
    def get_role(self) -> str:
        pass

    def save(self):
        cursor.execute("INSERT INTO users (id, username, role) VALUES (?, ?, ?)",
                    (self.id, self.username, self.get_role()))
        conn.commit()
