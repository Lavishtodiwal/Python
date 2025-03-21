import os 
fileName = input("Enter the file name->").lower().replace(" ","")
f= open(f"{fileName}.txt", "w+")
userInput = input("enter the some data to append-> ").lower().replace(" ","")
f.write(userInput)
f.seek(0)
show = input("Do you want to see the data of the file (yes/no) -> ").lower().replace(" ","")
if show == "yes" or show =="ok":
    print(f.read())
else:
    print("No Problem")
f.close()
delete = input(f"Do you want to delete {fileName}.txt file (yes/no)-> ").lower().replace(" ","")
if delete == "yes" or delete =="ok":
    os.remove(f"{fileName}.txt")
    print("Deleted Successfully!")
else:
    print("No Problem")
