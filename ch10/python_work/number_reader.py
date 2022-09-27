"""Demonstrating how to use json.load() to read a list of numbers and
effectively share data between programs."""
import json

filename = 'json_files/numbers.json'
with open(filename) as f:  # no need to specify 'r' mode, it is default
    numbers = json.load(f)

print(numbers)
