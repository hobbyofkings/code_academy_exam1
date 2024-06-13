# Inheritance with Shape Classes
# Objective: Create a base class `Shape` and two derived classes `Rectangle` and `Circle`.
# The `Shape` class should have an abstract method `area` that calculates the area of the shape.
# The derived classes should implement the `area` method.

# Details:
# - The `Shape` class should have an `__init__` method that initializes the shape with its dimensions.
# - The `Rectangle` class should be initialized with width and height.
# - The `Circle` class should be initialized with radius.
# - Both derived classes should implement the `area` method to calculate and return the area of the shape.


class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159265359 * self.radius ** 2


# Examples:
rectangle = Rectangle(4, 5)
circle = Circle(3)
print(rectangle.area())  # Expected: 20
print(circle.area())     # Expected: 28.274333882308138