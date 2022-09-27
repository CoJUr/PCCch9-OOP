"""Greeting a previously stored user, again utilizing the json module."""
import json

filename = 'json_files/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

