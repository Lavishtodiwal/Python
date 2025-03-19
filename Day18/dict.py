dict1 = {
    "name": "mohan",
    "class": "BCA",
    "college": "FIT College"
}
# for keys, items in dict1.items():  #this is used to print the output line wise
#     print(f"{keys}: {items}")


# if "name" in dict1:
#     print("yes it is available in the dict1") #check if the keys are no

# for x in dict1.items():
#     print(x)

#copy methods of the dictionary

# copyDict1 = dict1.copy()
# print(copyDict1)
# copyDict2 = dict(dict1)
# print(copyDict2)

    
college = {
    "student1": {
        "name" : "Ashish",
        "class" : "BCA",
    },
    "student2": {
        "name" : "Sahil",
        "class" : "BCA",
    },
    "student3": {
        "name" : "Lucky",
        "class" : "BCA",
    }
}
# print(college["student1"]["name"])
# print(college["student2"]["name"])
# print(college["student3"]["name"])

# for keys, items in college.items():
#     print(keys)
#     for y in items:
#         print(y,":",items[y])

for x, y in college.items():
    print(x)
    for i,j in y.items():
        print(i,":",j)