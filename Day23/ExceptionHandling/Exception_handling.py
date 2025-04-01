# errors 
# 1. compile time errors
# 2. run time errors
# 3. logical errors

try:
    num = int(input("enter anumber-> "))
    result = 10 /num
    print(f"result: {result}")
except ZeroDivisionError:
    print("you cant divide it with zero")
except ValueError:
    print("you cant divide it with string")



    