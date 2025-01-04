import json

file_path = './info.json'

with open(file_path, 'r') as file:
    data = json.load(file)

print(type(data))
print(data)
print(data["Tyler"])