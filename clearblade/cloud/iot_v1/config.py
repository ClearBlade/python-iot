#TODO: need to take this from users via some method and save them
import os

def get_auth_token():
    return os.environ.get("AUTH_TOKEN")

def get_system_key():
    return os.environ.get("SYSTEM_KEY")
