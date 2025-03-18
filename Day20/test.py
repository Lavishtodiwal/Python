# s = "python"

# reverseString = ""
# # for i in s:
# #     reverseString = i + reverseString
# # print(reverseString)

# print(" ".join(reversed(s)))

# for i in reversed(s):
#     reverseString = reverseString + i

# print(reverseString)

# for i in range(50):
#     if i ==0 :
#         continue
#     if i % 2 == 0:
#         print(i)

# for i in range(2,50,2):
    # print(i)

# a = 241
# # add = 0
# # for i in str(a):
# #     add += int(i)
# # print(add)

# add = sum(int(digit) for digit in str(a))
# print(add)

def reverse_seq(n):
    return list(range(n, 0, -1))
     

print(reverse_seq(5))