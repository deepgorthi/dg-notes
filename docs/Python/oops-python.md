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
##########################################
```

## Class Variables and Instance Variables

- Class variables are variables shared among all instances of the class. 
- Instance variables are unique to each instance of that class. 
- To access the `namespace` of the class instance, we can use
    ```python
    print(emp1.__dict__)
    # Output
    # {'first': 'First', 'last': 'Example', 'pay': 1040, 'email': 'First.Example@example.com'}
    ```
- To change a variable for a class and not any instance, we can use:
    ```python
    Employee.num_of_emps += 1
    ```

## Regular Methods, Class Methods and Static Methods

- **Regular methods** in a class automatically take the instance as the first argument.

- **Class methods** in a class automatically take the class as the first argument. 

  - Adding a decorator (`@classmethod`) before the method definition in the class makes it a class method. 
  - The decorator is altering the functionality of the method.
    ```python
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    # To change the raise_amount for all the class instances instead of just the instance, we can use:
    Employee.set_raise_amount(1.05)

    # We can also call the classmethod using the instance of that class and it will have the same effect on all the instances of that class. 
    emp1.set_raise_amount(1.05)
    ```

- Using Class methods as **Alternative Constructors**

  - We can use this class methods in order to provide multiple ways of creating our objects.
  - If there is a repeating part of the code that we are running in multiple instances of the class, we can define class methods to define that particular code and this is referred to as alternative constructor.

- **Static Methods** do not pass anything as the first argument.

  - While regular methods pass the instance of the class and class methods pass the class as the first argument, static methods do not expect the first argument to be either the class or the instance of that class. 
    ```python
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or if day.weekday() == 6:
            return False
        return True
    ```

## Inheritance - Creating Subclasses