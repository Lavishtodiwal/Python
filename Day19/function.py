# def greet(name):
#     print("Hii,",name )
#     greet(name)
# greet(input("enter your name => "))


#function with return value
"""
def add(a, b):
    return a + b

print(add(10,10))"""


#function  with variable arguements

def add_numbers(*args):
    print(args[1])
    return sum(args)
 

#print(add_numbers(1,2,3,4)) #this is used to input multiple values

# multiple keyword arguements (dict)

def info(**args):
    return args

result = info(name = "mukesh",age= 19, course = "BCA" )
# print(result)


#passing list in function

def listFunc(food):
    for items in food:
        print(items)

# listFunc(["Paneer Tikka", "Palak Paneer"])



# positional keyword and keyword arguements

def add(a,/,b):
    print(a)
    print(b)

# add ("sum","min") 
# this is position only argument and it can't be send as add(a = "sum", b = "min")


def add(a,*,b):
    print(a)
    print(b)

# add ("sum", b="min")
#in this 



#type of arguements in py
"""
1. positional args -> means it should be on position based parameter and args
2. keyword args    -> to overcome the issue of the positional args
3. default args
4. value based  (*args) and (*kargs)

"""



def fname(name,age): #here the name is the parameter 
    print(f"{name} and age is {age}")

# fname(age = 2, name = "Lavish")     #here given lavish is the argument


# below two are the value based args 
def add(*args):
    print(sum(args))
# add(1,2,3,4,5)

def info(**args):
    return args

result = info(name = "mukesh",age= 19, course = "BCA" )
# print(result)

#this lambda function works as function
result = lambda a : a * a
print(result(5))
