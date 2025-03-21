while True:
    print("1) Create new file")
    print("2) Display the file")
    print("3) Add a new item to the file")
    user = int(input("Make a selection 1, 2 or 3:"))
    match(user):
        case 1: 
            user_subject = input("Enter a school subject name: ")
            with open("Subject.txt", "w") as f:
                f.write(f"{user_subject}, ")
        case 2: 
            with open("Subject.txt","r") as f:
                print(f.read())
        case 3:
            with open("Subject.txt","a+") as f:
                new_subject = input("Enter a new subject name: ")
                f.write(f"{new_subject}, ")
                f.seek(0)
                print(f.read())
        case _:
            print("Please Enter a right choice from 1, 2, 3")
            break