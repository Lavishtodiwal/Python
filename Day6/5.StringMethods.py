#1.len -> to find the length of the string
print(len("hello python"))
#2. str.upper() -> to convert in the uppercase
str= "FIT College"
print(str.upper())
#3.str.lower() -> to convert in the lowercase
print(str.lower())
#4.str.capitalize() -> to convert each sentence first letter capital
print(str.capitalize())
#5.str.title() -> to convert eact word first letter capital

print(str.title())


text = "Jai Shree Ram"
#6. str.strip is used to remove anything from the first and last not from the middle 
print(text.strip("m"))

#7.Each letter is assigned to an index number to identify its position including space, index starts from 0 not from 1
#8. 
print(str[7:10]) #this is called slice
print(text[0:13])

#there are three type of strings in docstring

a= 'hello'
b= "hello"
c= '''hello
    world'''
d= """hello
    world"""

"""this is also use for multiple line comment. and also used as DocString"""