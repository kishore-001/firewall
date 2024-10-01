import json
import os

import bcrypt

# File to store user credentials
CREDENTIALS_FILE = "/home/black/projects/firewall/scripts/opt/credential.json"


def create_user(username, password):
    """Creates a new user with a hashed password."""
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Check if credentials file exists
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as f:
            users = json.load(f)
    else:
        users = {}

    # Store the user credentials
    users[username] = hashed.decode("utf-8")

    with open(CREDENTIALS_FILE, "w") as f:
        json.dump(users, f)

    return "User created successfully."


def authenticate_user(username, password):
    """Authenticates a user by comparing the hashed password."""
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as f:
            users = json.load(f)

        if username in users:
            hashed = users[username].encode("utf-8")
            if bcrypt.checkpw(password.encode("utf-8"), hashed):
                return "Authentication successful."
            else:
                return "Incorrect password. Try again."
        else:
            return "User not found."
    else:
        return "No users registered."
