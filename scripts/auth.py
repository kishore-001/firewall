# scripts/auth.py
import json
import os

import bcrypt

CREDENTIALS_FILE = "credentials.json"


def load_users():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_users(users):
    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(users, f)


def create_new_user(username, password):
    users = load_users()

    if username in users:
        return False  # User already exists

    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    users[username] = hashed.decode("utf-8")
    save_users(users)
    return True


def authenticate(username, password):
    users = load_users()

    if username in users:
        stored_hash = users[username].encode("utf-8")
        if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            return True
    return False
