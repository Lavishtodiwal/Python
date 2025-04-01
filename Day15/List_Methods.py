a = [1,2,3,4,5,3,3,3,3]
b = [6,7,8,9,10,1,2,3]
# a.append(11) # append items to the  end of the list 
# a.extend(b) # extends items of b in list a
# a.insert(0, 11) # inserts the value at 0 index and it will not delete any items
# a.remove(3) #this removes the data from the list a
# a.pop(0) #this removes the element from the 0 index and returns that popped value
# a.clear() #this clear complete the list returns empty list
# print(a.index(5)) # this returns the index no. of the item in list
# print(a.count(3)) #returns the count of the items in list# sort the list in ascending order
# a.reverse() # reverse the items in list
# print(a.copy()) #copies the list 

# ---------finding, 

# print(min(a)) #returns the min number
# print(max(a)) #returns the max number
#finding common items

# A = set(a)
# B = set(b)
# C = A.intersection(B)
# print(list(C)) # returns the common numbers from the lists

# nested_list = ['a','e','i','o','u',a,['b','d','g']]
# print(nested_list[5][2])
# print(nested_list)


# num = list(range(1,10,1)) # returns the numbers from the 1 to 9
# print(num)

#method 1
# square = []
# for i in range(1,11):
#     square.append((i ** 2))
# print(square)

#method-2 
square = [i ** 2 for i in range(1,11)] #ont line logic 
# method of this--
# [operation, loop, condition(optionale)]
print(square)


print(a)