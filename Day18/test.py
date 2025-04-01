a = {
    "name": "Ashish",
    "class": "BCA",
    "subjects":{
        "sub" : "Hindi",
        "marks": 90
    }
}

for key, values in a.items():
    print(key)
    # print(values)
    if key == "subjects":
        
        for i , j in values.items():
            print(i,j)