from copy import deepcopy

from uuid import uuid4

class Employee:
    def __init__(self, firstname, last_name):
        self.firstname = firstname
        self.last_name = last_name
        self.salary = None
        self.title = None
        self.employee_id = None

    def add_employee_id(self, employee_id):

        if not self.employee_id:
            self.employee_id = employee_id
        else:
            print("Employee already has Id")

    def add_salary(self, salary):
        if not self.salary:
            self.salary = salary
        else:
            print("Employee already has salary")

    def add_title(self, title):
        if not self.title:
            self.title=title
        else:
            print("Employee already has a title")


Horace = Employee("Horace", "Akpan")

#print(Horace.firstname)

print(Horace.employee_id)

Horace.add_employee_id(employee_id=uuid4())
Horace.add_title(title="BackEnd Developer")
Horace.add_salary(salary=2500.00)
print(Horace.__dict__)

