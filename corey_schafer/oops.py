#python object oriented programming

class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('test', 'user', 60000)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'corey.schafer@gmail.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.user@gmail.com'
emp_2.pay = 60000
print(emp_1.email)
print(emp_2.email)
print(emp_1.first)
print(emp_2.first)
print(emp_1.last)
print(emp_2.last)
print(emp_1.pay)
print(emp_2.pay)
print(emp_1.__dict__)  # prints the attributes of emp_1
print(emp_2.__dict__)  # prints the attributes of emp_2

print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_2.fullname())