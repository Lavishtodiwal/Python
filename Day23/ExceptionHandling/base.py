a = input("Enter a number-> ")
print(f"The table of the {a}: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}" )
except Exception as e:
    print(f"Please Give input in the for of int")
print("End of the program")