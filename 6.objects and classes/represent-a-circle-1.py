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


circle = Circle(1) #area of a circle 

print(circle.area())
print(circle.perimeter()) 