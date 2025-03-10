# s = {'a': "lavish", 'b': "aashish", 'c': "sahil"} #basic dictionary
# s['d'] = "palak" # add elements to the dict
# s['e'] = "Mansi"
# s['e'] = "shruti" #update the existing value
# # del s['e'] # remove the item with the help of del using key:value and also can delete entire dictionary
# # pop = s.pop('b') #in the pop enter the key of the item that we want to remove
# # s.popitem() #used to remove the item from the end
# # s.clear() # used to clear the entire dictionary
# print(s)

# fruits = {
#     'name': "apple",
#     'price': 150,
#     'discount' : '30%'
# }
# fruits.update({'quantity': 1500}) 
# # print(fruits)

# appledetails = fruits.copy()
# print(appledetails)
# print(appledetails.fromkeys('name'))

# s = {1: "lavish", 3: "sahil", 9:"palak", 5:"op"}
# print(s)



dict1 = {
    1: "apple",
    2: "banana",
    3: "grapes"
}
print(dict1.get(11, "not found")) #return if not found
print(dict1.keys())
print(dict1.values())
print(dict1.items())

a = print(dict1.pop(1)) 
print(a) #after some time a will become none

dict1.update({4: "pine apple"})
print(dict1)
print(dict1.items)