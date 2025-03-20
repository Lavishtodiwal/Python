subjects = ["hindi", "english","maths", "chemistry","physics","art" ]
print(subjects)
user = input("Enter the subject name that u want to delete-> ")
subjects.remove(user)
print(subjects)