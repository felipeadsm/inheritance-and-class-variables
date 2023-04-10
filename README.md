# Inheritance and Class Variables

### Objectives

- Explain the difference between class variables and instance variables

### Introduction

- Inheritance is a powerful tool in object-oriented programming. It allows us to create a new class that is a
  specialized version of an existing class. Inheritance is a way to reuse code and to express an is-a relationship. For
  example, a `FirstClass` is a type of `BaseClass`, so a `FirstClass` class could inherit from an `BaseClass` class. In this lesson, we'll
  look at how inheritance works in Python.

- `BaseClass` has a class variable called database, this variable indicates the database that the class uses. The
  `FirstClass` class inherits from `BaseClass`, so it also has access to the `database` class variable;
```python
class BaseClass:
    database = Database()

    def __init__(self, name):
        self.name = name
        self.instance_database = Database()

    def __str__(self):
        return self.name
```

- Too, we can access the `database` class variable using an instance of the `FirstClass` class:

```python
from base_class import BaseClass

class FirstClass(BaseClass):
    def __init__(self):
        super().__init__('FirstClass')

def main():
    first_class = FirstClass()
    print(first_class.database.data)

if __name__ == '__main__':
    main()

# output:
# [5, 4, 3, 2, 1]
```