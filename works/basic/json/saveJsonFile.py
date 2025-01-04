import json

data = {
    "Olivia" : {
        "gender": "female",
        "age" : 25,
        "hobby" : ["reading", "music"]
    },
    "Tyler" : {
        "gender": "male",
        "age" : 28,
        "hobby" : ["development", "painting"]
    }
}

file_path = "./info.json"

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file)
    #json.dump(data, file, indent="\t", ensure_ascii=False)

