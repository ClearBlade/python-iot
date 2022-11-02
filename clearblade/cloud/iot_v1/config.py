#TODO: need to take this from users via some method and save them
import os
from exceptions import UnconfiguredEnvironment

def get_auth_token():
    auth_token =  os.environ.get("AUTH_TOKEN")
    if not auth_token:
        raise UnconfiguredEnvironment()

def get_system_key():
    system_key =  os.environ.get("SYSTEM_KEY")
    if not system_key:
        raise UnconfiguredEnvironment()
