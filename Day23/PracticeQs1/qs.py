with open("practice.txt","r") as f:
    # f.write("Hi everyone\nwe are learning File IO\nusing java\nI like Programming in java")
    data = f.read()
    # print(type(data))
    f.close()

new_data = data.replace("java", "python")
# print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

with open("practice.txt","r") as f:
    data = f.read()
    print(data)
res=data.find("learning")
print(res)