lines = ["Lavish\n", "Sahil\n", "Ashish\n", "Ashu\n", "Arnav"]
with open("Names.txt", "w+") as f:
    f.writelines(lines)
    f.seek(0)
    print(f.read())

user = input("Enter a name-> ")
with open("Names.txt", "a+") as f:
    f.write(f"\n{user}")
    f.seek(0)
    print(f.read())