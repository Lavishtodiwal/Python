try: 
    file = open("demo.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("file not found")

finally: #this block of code will run definately 
    file.close()
    print("file operation competed")