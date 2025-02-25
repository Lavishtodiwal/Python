name = input("Enter your Full Name->")
age = int(input("Enter your age->"))
if age >= 22:
    score = int(input("Enter your Credit Score->"))
    if score < 900 and score > 100 :
        salary = int(input("Enter your salary->"))
        if salary >= 15000 and score >= 700:
            print(f"Congratulations {name}, You are eligible for the Loan")
        elif salary < 15000 and score >= 700:
            print(f"Sorry {name}, Your salary should be more than 15000 to get a loan")
        elif salary >= 15000 and score < 700:
            print(f"Sorry {name}, Your credit score should be more than 700 to get a loan")
        else:
            print(f"Sorry {name}, Your salary and credit score is not enough to get a loan")
    else: 
        print(f"Hey, {name} You can't enter a unvalid credit score")
else : 
    print("You are not eligible for the loan because your age is less than 22")
 