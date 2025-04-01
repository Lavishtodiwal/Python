# def fact(n):
#     if n == 0 :
#         return 1
#     else: 
#         return n* fact(n-1)

# print(fact(1))


# n = [1,2,3,41,5]
# max = 0 
# for i in n:
#     if max < i:
#         max =i
    
    
# print(max)


# a = "lavish"
# count =0
# for i in a:
#     if i.lower() in "aeiou":
#         count += 1

# print(count)

s = "pythn"

def vw(s):
    return sum(1 for i in s if i.lower() in "aeiou" )
vw(s)

n = 9

if n > 1:
    for i in range(2,n):
        if n % i ==0 :
            print("not prime")
            break
    else:
        print("prime")
        

    