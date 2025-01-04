import pickle

some_dict = {"id": 5, "name" : "test"}

data = pickle.dumps(some_dict)

new_dict = pickle.loads(data)

print(some_dict)
print(new_dict)