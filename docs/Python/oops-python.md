# Python Object-Oriented Programming

## Classes and Instances

- *`Self` can be described as the instance reference in the class.*
- Each method in the class automatically takes the instance as the first argument.
- Even though `self` is the standard, anything can be used. 
- `__int__` is the constructor declaration for a class.
- Instead of initializing each object of the class, we are using self as the reference to the object instance. 
- If we are not declaring the object instance when defining the class, then we need to instantiate every property of that instance manually. 
- `emp1.fullname()` is the same as `Employee.fullname(emp1)`


```python
##########################################
# Manual Object instantiation
##########################################
class Employee:
    pass

emp1.first = 'First'
emp1.last = 'Example'
emp1.pay = 1000
emp1.email = 'First.Example@example.com'

emp2.first = 'Second'
emp2.last = 'Example'
emp2.pay = 1000
emp2.email = 'Second.Example@example.com'

##########################################

##########################################
# Using self for creating object instance
##########################################
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

print(emp1.email)
# Outputs the email: First.Example@example.com
##########################################
```

