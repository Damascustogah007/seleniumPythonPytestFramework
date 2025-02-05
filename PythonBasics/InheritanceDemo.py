#Creating parent class
class Employee:
    def __init__(self, empname, emprollno):
        self.empname = empname
        self.emprollno = emprollno

    def show(self):
        return f'{self.empname} - {self.emprollno}'


#Creating child class
class QA(Employee):
    def __init__(self, dept, empname, emprollno):
        self.dept = dept
        Employee.__init__(self, empname, emprollno)

    def showDetails(self):
        return f'{self.empname} - {self.emprollno} - {self.dept}'


#Creating child2 class

class DEV(Employee):
    def __init__(self, dept, empname, emprollno):
        self.dept = dept
        Employee.__init__(self, empname, emprollno)

    def getDept(self):
        return f'{self.empname} - {self.emprollno} - {self.dept}'

#Creating the object for child class
qa = QA("IT", 'Charles', 56)
print(qa.showDetails())

dev = DEV("Developer", 'Solomon', 23)
print(dev.getDept())