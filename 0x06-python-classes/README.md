# Python - Classes and Objects
*Object Oriented Programming* (*OOP*) is a way of organizing your programs using *objects*, reusable structures that contain data and functionality. The main concepts of *OOP* are *classes* (the type), and *objects* (instances of the type).

Objects can store *fields* (variables), and *methods* (functions), or collectively, *attributes*
Fields can belong the class (class variables), or they can belong to each instance (instance variables).

## Usage example
Here, we define a simple `class` named `Example` with fields and methods. Then, an object is created, and its method executed.
```
class Example:
      # Fields (variables)
      # Class variables
      num = 0

      # Object variables are declared using self
      def __init__(self, name):
      	  self.name = name
      
      # Methods
      def say_hi(self):
      	  print('Hello, how are you?')

      # Method that belongs to the class, and not the object
      @classmethod
      def get_num():
      	  return num

p = Person()
p.say_hi()
```

### The `__init__` method
The `__init__` method runs as soon as an object is created (instantiated), useful for an object's initial setup.

### The `@classmethod` decorator
Think of a decorator as a function wrapper that does something before the inner function.

### The double underscore prefix
All members are public. To make it private (i.e. accessible only from within the class or object), use double underscores: `__this_is_a_private_variable`

## Inheritance
Think of inheritance as implementing a *type and subtype* relationship between classes. This is used to identify types with common attributes, and defining a parent type where the common attributes can be inherited from.
### Usage Example
```
class Parent:
      # parent attributes defined here

class Child(Parent):
      # parent attributes from Parent
      # child attributes defined here
```
*NB: you have to call `Parent.__init__(self, ...)` in the child class/classes. to initialize the `Parent` attributes in the `Child`

### You can inherit multiple classes
...By providing a tuple of class Names in the Subclass definition:
`class Child(Parent1, Parent2, Parent3):`

## Tasks:
1. `0-square.py` - defines an empty class `Square`
2. `1-square.py` - defines a `Square` class with a private attribute
3. `2-square.py` - defines a `Square` class with optional private attribute
4. `3-square.py` - defines a `Square` class with optional private attribute and public instance method.
5. `4-square.py` - based on `3-square.py`, adds a public instance method, `area`.
6. `5-square.py` - based on `4-square.py`, adds a method to print the square using #.
7. `6-square.py` - based on `5-square.py`, adds a position instance attribute and its getter and setter methods.
