"""1. key -value pair
2. unorderd -before 3.7 version and after that it becomes ordered
3. dynamic"""


a = {
    "Name" : "Lavish",
    "Age": 20,
    "Course" : "BCA",
    "marks" : [1,2,3,4,5]
}

# a["College"] = "FIT collge" # add the items in dict
# a["College"] = "F.I.T. collge" # update the items in dict

# del a["marks"] # deletes the items from the dict

#--------------- Methods ---------------
# print(a.get("Name2","Not Found")) #pass the key in the get func and it returns the value of that key in case of not found it returns the none and after , is that in case of the key is not available it returns  this msg "not found"

# print(a.keys())# returns the keys of the dict
# print(a.values()) # returns the value of the dict
# print(a.items()) #returns the entire dict in the form of the touple

# print(a.pop("Name2", "not found")) # removes the items from the list using key nae in case not found it will print the not found
# print(a.popitem()) #delete the items from the end and returns taht removed item
# a.clear() # clear the entire dict

# dict comprehnsive
# square = {x: x**2 for x in range(1,11)}
# print(square)

# lang = {
#     "name": "python",
#     "use" : {
#         "name": "Machine Learning"
#     }
# }
# print(lang)




print(a)