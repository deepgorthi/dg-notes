class Employee:
    def __init__(self, first, last, pay):
        self.first = first  
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@example.com'
        # This can also be something like self.fname = first

    def fullname(self):
        return f'{self.first} {self.last}'

emp1 = Employee('First', 'Example', 1000)
emp2 = Employee('Second', 'Example', 1000)

print(emp1.fullname())