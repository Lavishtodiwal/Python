import json
data = {"name":"Ashish", "Age":25}

with open("data.json", "w") as file:
    d = json.dump(data, file) #dump the data to the json file 
    print(type(d))


with open("data.json", "r") as f:
    userInfo = json.load(f) #load is used extract the data from the json file 
    print(type(userInfo))
    print(userInfo)


import json
data = {"name":"Ashish", "Age":25}

# dumps is used to dump the data to the file without the file handling
d = json.dumps(data)
print(type(d))


# 
userInfo = json.loads(d) #loads is used extract the data from the json file without file handling
print(type(userInfo))
print(userInfo)