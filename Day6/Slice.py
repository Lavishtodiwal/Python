 #     012345
name= "python"
#   -5,-4,-3,-2,-1   
# print(name[2:4]) -> th
# print(name[:7]) -> python
# print(name[2:])-> thon
# print(name[1:-3])

#in this case negetive indexing will be considered as the positive for e.g. in case of index 1 and negetive will considered as positive index but it will never run backword means not from -1 to -5 and not from 5 to 1 so in these case this will show the blank space
# print(name[-4:-1])
# print(name[0:5:1]) #-> 
#in the above case the string will print from 0 to 
# print(name[-3:-6:-1]) -> in this it will go to the opposite because we give the -1 in the steps 
# print(name[::-2]) 
#same as above but it wil go from backword 2 steps 

print(name[2:-4:-1])