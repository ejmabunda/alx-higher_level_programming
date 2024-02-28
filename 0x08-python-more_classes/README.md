This project explores more concepts in Object-oriented Programming by creating a Rectangle class.

# Rectangle Class

The `Rectangle` class is a Python implementation that defines a rectangle with width and height attributes. It includes features for retrieving and setting these attributes, calculating the area and perimeter, as well as providing a visual representation of the rectangle using the `print()` and `str()` methods. Additionally, the class keeps track of the number of instances created and prints a farewell message upon instance deletion.

## Class Attributes

- `number_of_instances`: Initialized to `0`, this class attribute is incremented during each new instance instantiation and decremented during each instance deletion.
- `print_symbol`: Initialized to `#`, this class attribute is used as a symbol for string representation.

## Constructor

The class is initialized using the constructor `__init__(self, width=0, height=0)`, which allows for optional specification of the initial width and height of the rectangle.

## Properties

- `width`: A private attribute with a property getter and setter to retrieve and set the width of the rectangle. Raises `TypeError` if the width is not an integer and `ValueError` if it is less than `0`.
- `height`: A private attribute with a property getter and setter to retrieve and set the height of the rectangle. Raises `TypeError` if the height is not an integer and `ValueError` if it is less than `0`.

## Methods

- `area(self)`: Public instance method that returns the area of the rectangle.
- `perimeter(self)`: Public instance method that returns the perimeter of the rectangle. If either width or height is equal to `0`, the perimeter is `0`.
- `__str__(self)`: `print()` and `str()` methods that print the rectangle using the character specified by `print_symbol`. If either width or height is equal to `0`, it returns an empty string.
- `__repr__(self)`: Returns a string representation of the rectangle that can be used to recreate a new instance using `eval()`.
- `__del__(self)`: Destructor method that prints the message "Bye rectangle..." when an instance of `Rectangle` is deleted.

## Static Methods

- `bigger_or_equal(rect_1, rect_2)`: Static method that returns the rectangle with the larger area between `rect_1` and `rect_2`. Raises `TypeError` if either argument is not an instance of `Rectangle`.

## Class Methods

- `square(cls, size=0)`: Class method that returns a new `Rectangle` instance with equal width and height, specified by the `size` parameter.

## Example Usage

```python
# Example Usage
r = Rectangle(3, 4)
print(r.area())          # Output: 12
print(r.perimeter())     # Output: 14
print(str(r))            # Output: "###\n###\n###"
del r                    # Output: "Bye rectangle..."
print(Rectangle.number_of_instances)  # Output: 0

# Static Method Usage
r1 = Rectangle(4, 5)
r2 = Rectangle(3, 6)
larger_rect = Rectangle.bigger_or_equal(r1, r2)
print(larger_rect.area())  # Output: 20

# Class Method Usage
square_rect = Rectangle.square(size=5)
print(square_rect.width)   # Output: 5
print(square_rect.height)  # Output: 5
