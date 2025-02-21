      # 012345
name = "python"
print(name[2:4:-1]) #in case of the negetive steps starting value should be greater than ending value

print(name[4:2:-1]) #like this, it will show the right ans because it reads from right to left 

a = "  kaaju   "
print(a)
print(a.lstrip(" ")) # lstrip for removing white space from the left
print(a.rstrip(" "))# rstrip for removing white space from the right 
print(a.strip(" ")) #l strip for removing white space from the both side




a = "hello world"
print(a.swapcase()) #it is used to convert in the opposite case
print(a.replace("world", "python!")) # this is used to replace any word or char with another word or key
print(a.replace("wo", "py")) # this is used to replace any word or char with another word or key

print("-".join(["Hello","World"])) 
print("----".join(["Hello","World","of", "Python"])) # this is used to join strings using some chars or maybe sign 

print(a.split()) #this is used to split the words sepratelly i.g. "Hello World" -> ['hello', 'world']
print(a.rsplit('o')) #this is used to seprate the strings based on the char given in the parenthesis

str = """hello hey 
this is me yes me """
print(str.splitlines()) # this is used to seprate multiple line of strings

# print(a.partition(''))

#string checking 
print(a.startswith("hello")) # used to check string  starts with that letter, word or not
print(a.endswith("world")) # used to check string ends with that letter, word or not
print(a.isalpha()) # used to check the string has all words are alphabets or not, here it is showing error because hello world has a space btwn them 
print(name.isalpha())

print(a.isdigit()) #used to check the string has all words are digits or not
b = "1213"
print(b.isdigit()) #used to check the string has all words are digits or not
print(a.islower()) # return true if the strings are in the lowercase 
print(a.isupper()) # return true if the strings are in the uppercase 
print(b.isalnum()) # return true if the strings are in the form of the alpha + numeric

# finds     

print(a.find("world")) 
print(a.find("r")) #this is used find the index of any char or strings
print(a.rfind("o")) #same as find
print(a.count("n"))# it is used to count the no of times occur the character in the string


#String formatting

print(a.center(20, "*")) # center the string using * total 20 chars will take place
print(a.center(20, "^")) # center the string using ^ total 20 chars will take place but only one char used in parenthesis

print(a.ljust(20,"*")) #ljust is used to adjust the string in the left and remaining filled with astericks(*)
print(a.rjust(20,"*"))#rjust is used to adjust the string in the right and remaining filled with astericks(*)

print("87".zfill(10)) #zfill is used to fill all 10 spaces using 0 as i given the total spaces is 10 and here the 87 are two and the  remaining part from the left will filled by  the 0


#encoding and decoding

decoded = a.encode('utf-8') #converted to utf-8 encoding
print(decoded)
encoded = decoded.decode('utf-8') # decoded from encodded 
print(encoded)

print(a.isprintable()) # checks it is printble or not 

c = " "
print(c.isspace()) #
