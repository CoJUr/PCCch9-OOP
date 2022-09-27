"""Using json.dump() and json.load() to store and read numbers"""
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'json_files/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

    