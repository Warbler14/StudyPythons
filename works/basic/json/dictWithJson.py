import json

some_dict = {"id": 5, "name" : "test"}

data = json.dumps(some_dict)

print("dict : {}".format(data))

print("https://docs.python.org/ko/3/library/json.html")

# see marshal pickle
# https://docs.python.org/ko/3/library/marshal.html#module-marshal
# https://docs.python.org/ko/3/library/pickle.html#module-pickle