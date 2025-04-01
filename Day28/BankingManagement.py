class User:
    def __init__(self, userName, userDOB, userFather, userPAN, userAcNo):
        self.userName = userName
        self.userDOB = userDOB
        self.userFather = userFather
        self.userPAN = userPAN
        self.userAcNo = userAcNo
        self.balanceAmount = 0  # Initialize balance to 0

    def credit(self, amount):
        self.balanceAmount += amount
        print(f"₹{amount} credited to your account. Current Balance: ₹{self.balanceAmount}")

    def debit(self, amount):
        if amount > self.balanceAmount:
            print("Insufficient funds!")
        else:
            self.balanceAmount -= amount
            print(f"₹{amount} debited from your account. Current Balance: ₹{self.balanceAmount}")

    def disp(self):
        print("\n\t\tAccount Details")
        print(f"Account Number: {self.userAcNo}")
        print(f"Name: {self.userName}")
        print(f"D.O.B: {self.userDOB}")
        print(f"Father's Name: {self.userFather}")
        print(f"PAN Number: {self.userPAN}")
        print(f"Current Balance: ₹{self.balanceAmount}")


# Main program
userAcNo = 1000000000

while True:
    inp = input("Would you like to create an account in our bank (yes/no)? ").strip().lower()
    if inp == "yes":
        print("\n\tWelcome to XYZ Bank")
        userName = input("Enter your Name: ").strip()
        userDOB = input("Enter your D.O.B (dd:mm:yyyy): ").strip()
        userFather = input("Enter your Father's Name: ").strip()
        userPAN = input("Enter your PAN No.: ").strip()
        user = User(userName, userDOB, userFather, userPAN, userAcNo)
        userAcNo += 1

        while True:
            action = input("\nChoose an action: \n1. Display Account Details\n2. Credit Money\n3. Debit Money\n4. Exit\nEnter your choice: ").strip()
            if action == "1":
                user.disp()
            elif action == "2":
                amount = float(input("Enter amount to credit: ₹"))
                user.credit(amount)
            elif action == "3":
                amount = float(input("Enter amount to debit: ₹"))
                user.debit(amount)
            elif action == "4":
                print("Thank you for banking with us!")
                break
            else:
                print("Invalid choice. Please try again.")
    elif inp == "no":
        print("Thank you! Have a great day!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")