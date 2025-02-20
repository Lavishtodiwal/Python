# firstName = input("Enter the first Name->")
# surName = input("Enter the Surname->")
# combined = firstName + " " + surName
# print(combined)
# print("the length of the name is : ", len(combined))

firstName = input("Enter the first Name in lowercase->")
surName = input("Enter the Surname in lowercase->")
combined = firstName.title() + " " + surName.title()
print(combined)
print("the length of the name is : ", len(combined))