# 0x0A. Python - Inheritance

## Overview
In this project, I delve into the intricacies of inheritance in Python, aiming to master concepts such as superclass, subclass, method and attribute inheritance, multiple inheritance, and the use of built-in functions like `isinstance`, `issubclass`, `type`, and `super`.

## Project Structure
I've organized the project into multiple tasks, each implemented in a separate Python script. Corresponding test files for each task reside in the 'tests' folder. The project directory structure is as follows:

- **0-lookup.py**: I've crafted a function that returns the list of available attributes and methods of an object.
- **1-my_list.py**: I've developed a class `MyList` that inherits from `list` and includes a method to print the sorted list.
- **2-is_same_class.py**: I've created a function that returns True if an object is exactly an instance of a specified class.
- **3-is_kind_of_class.py**: I've implemented a function that returns True if an object is an instance of, or inherits from, a specified class.
- **4-inherits_from.py**: I've written a function that returns True if an object is an instance of a class that inherited from a specified class.
- **5-base_geometry.py**: I've defined an empty class `BaseGeometry`.
- **6-base_geometry.py**: I've expanded on `BaseGeometry`, adding a method that raises an exception.
- **7-base_geometry.py**: I've enhanced `BaseGeometry` with a method for validating integers.
- **8-rectangle.py**: I've crafted a class `Rectangle` that inherits from `BaseGeometry` and includes width and height validation.
- **9-rectangle.py**: I've extended `Rectangle` with an implemented area method and a customized string representation.
- **10-square.py**: I've designed a class `Square` that inherits from `Rectangle` and includes size validation.
- **11-square.py**: I've refined `Square` with a customized string representation.

## Usage
To execute the test cases for each task, run the following command in the project directory, not all tasks include tests:

```
python3 -m doctest ./tests/*
```

You can check the code style using the `pycodestyle` tool:

```
pycodestyle *.py
```