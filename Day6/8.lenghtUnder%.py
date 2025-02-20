firstName = input("Enter the first name->")
length = len(firstName)
if length < 5 :
    surname= input("Enter the surname->")
    name = firstName + surname
    print(name.upper())
else:
    print(firstName.lower())