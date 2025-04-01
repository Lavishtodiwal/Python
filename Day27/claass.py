class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(f"name: {self.name}'s id: {self.id}")


student1 = Student("Ashish", 123)

student1.display()

# hospital managemenk