
#----opening a file in py----------

# f = open("demo.txt","r")
# data = f.read() #read the entire data in the file
# data = f.read(5) #read the data upto 5 positions in the file
# data = f.readline() #read the data line by line in the file
# print(data) 
# f.close() #this is neccessory part or we can say good practice to close the file 
 
#----writing into the file -------


# f = open("demo.txt","w") #here w is used for write and this will overwrite all the data from that file 
# f.write("This is over write by the python's file handling technique")

# f = open("demo.txt","a") #here a is used for write the data at the end and it does not override that file 
# f.write("\nThis is append by the python's file handling technique")
# f.close() 


# + methods

# f = open("demo.txt", "r+") # r+ is used to read and overwrite the file from the starting
# f.write("That")
# print(f.read())
# f.close

# --------------------2nd Method of performing the file handling -----------------------------

# with is used to remove the error exception in case we dont use the .close so here use of with and here is not need to write the close the file 
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

#to delete a file use os import and use it 

import os
with open("sample.txt", "w+") as n:
    n.write("This is the remove function use")
    print(n.read())
    # n.close()
    os.remove("sample.txt")