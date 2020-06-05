class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first  
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@example.com'
        # This can also be something like self.fname = first
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    

print(Employee.num_of_emps)

# To change the raise_amount for all the class instances instead of just the instance, we can use:
Employee.set_raise_amount(1.05)
    
emp1 = Employee('First', 'Example', 1000)
emp2 = Employee('Second', 'Example', 1000)

print(emp1.email)
print(emp1.fullname())
print(Employee.fullname(emp1))
print(f"Pay before raise - {emp1.pay}")
emp1.apply_raise()
print(f"Pay after raise - {emp1.pay}")
print(emp1.__dict__)
print(Employee.num_of_emps)


