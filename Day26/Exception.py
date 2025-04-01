try:
    a = 10
    print(a/0)
except Exception as e:
    print(e) #prints the error
    # print(type(e))
    # print(e.__class__) # they both return the <class 'ZeroDivisionError'>
    
else: # this is only execute after the execution of the try block
    print("divisible by something is done")

finally:
    print("well done, you learn the exception handling")