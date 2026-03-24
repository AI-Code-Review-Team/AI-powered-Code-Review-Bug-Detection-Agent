import sqlite3
import pickle
import hashlib

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def load_session(data: bytes):
    return pickle.loads(data)

SECRET_KEY = "hardcoded_secret_123"
