class Student:
    def __init__(self, name , id):
        self.name = name
        self.id = id
    def disp(self):
        print(f"Name : {self.name}")
        print(f"Id: {self.id}")



student1 = Student("lavish", 120)
student1.disp()