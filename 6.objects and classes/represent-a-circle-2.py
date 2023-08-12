class Circle:
    """Represents a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return 3.14 * self.radius**2

    def perimeter(self):
        """Calculates the perimeter of the circle."""
        return 2 * 3.14 * self.radius

# Creating a circle object
circle = Circle(int(input("Enter the value"))) # user input 

print("Circle with radius", circle.radius)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())