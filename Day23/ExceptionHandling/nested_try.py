try: 
    num1 = int(input("enter num1-> "))
    num2 = int(input("enter num2-> "))
    try:
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("you can't divide with0")
except ValueError:
    print("Please give valid input")