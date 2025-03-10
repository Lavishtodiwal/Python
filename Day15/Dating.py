while True:
    agree = input("Would you like to join us? (yes/no) -> ").strip().lower()
    match agree:
        case "yes":
            FullName = input("Enter your Full name: ").title().strip()
            if FullName.isdigit() == False :
                age = int(input("Enter your Age: "))
                if age < 42 and age > 14:   
                    email = input("Enter your email: ")
                    gender = input("Enter your gender (male/female/others): ")
                    mobileNo = input("Enter your mobile number: ")
                    mobileNo = input("Enter your mobile number: ")

                    while True:
                        if mobileNo.isnumeric() and len(mobileNo) == 10:  # Use built-in len() function
                            print("Thank you! Mobile number is valid.")
                            break
                        else:
                            print("Please enter a valid Indian mobile number with 10 digits:")
                            mobileNo = input("Enter your mobile number: ")
                    preference = input("which gender do u want to go with date (male/female)->")
                    print(f"Nice Choice,  {FullName}")
                    print("Let's discuss about your preferences :) ")
                    print("what would you like to drink?")
                    print("Coffee","Tea", "Other", sep="\n")
                    choice =input("enter your choice->").strip().lower()
                    match choice:
                        case "coffee":
                            print(f"You selected Coffee for your partener, Nice choice {FullName}")
                        case "tea":
                            print(f"You selected Tea for your partener, Nice choice {FullName}")
                        case _ :
                           print(f"you selected {choice} for your partener :) ")
                    userInfo= {
                        "Name" : FullName,
                        "Age": age,
                        "Email": email,
                        "Gender" : gender,
                        "Choice" : choice
                    }
                    for key, value in userInfo.items():
                        print(f"{key} : {value}")
                else:
                    print("Sorry you are not eligible")
            else:
                print("Please enter the right name")
        case "no":
            print("Thank you! Maybe next time.")
        case _:
            print("Invalid response. Please enter 'yes' or 'no'.")
    break
