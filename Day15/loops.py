fruits = ["apple", "banana", "grapes"]
price = ["150", "60", "250"]
for i in fruits: #here it will check all the items in list and print all the items from the list
    print(i)
# for i in range(10): #here i will take numbers from 10
#     print(f" iterantion : {i}") 



# for i in range(10):
#     if i == 5:
#         break
#     print(f"iteration: {i}")

# for i in range(10):
#     if i == 2:
#         continue #skips the current iterartion and moves to the next 
#     print(i)

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    #enumrates gives both list items and also index of that list

for fruit, price in zip(fruits, price): #Iterates over multiple iterables in parallel.
    print(f"{fruit}: {price}")

count = 1
while count <= 10 :
    print(count)
    count +=1