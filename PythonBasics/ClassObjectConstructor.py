#Class in python
class Student :
    # def __init__(self, name, age):
    name = 'Charles'
    age = 67

    def show(self):
        return f'my name is {self.name}, and I am {self.age}'

# student = Student('Charles', 56)
student = Student()
print(student.show())

#Constructor lass in python

class Student :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f'my name is {self.name}, and I am {self.age}'

student = Student('Charles', 56)
print(student.show())