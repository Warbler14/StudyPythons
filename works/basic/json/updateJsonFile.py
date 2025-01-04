import json

file_path = "./info.json"

with open(file_path, 'r') as file:
    data = json.load(file)

data["Olivia"]["age"] = 26
data["Olivia"]["hobby"].append("take a picture")
data["Tyler"]["age"] = 29
data["Tyler"]["hobby"].append("travel")

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent="\t")
