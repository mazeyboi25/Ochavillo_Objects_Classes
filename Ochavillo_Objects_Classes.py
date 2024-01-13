import math

class Circle:
    def __init__(self):
        # Prompt the user for the radius input
        self.radius = float(input("Enter the radius of the circle: "))

    def area(self):
        # Calculate and print the area of the circle
        circle_area = math.pi * self.radius**2
        print(f"Area of the circle with radius {self.radius}: {circle_area:.2f}")

    def perimeter(self):
        # Calculate and print the perimeter (circumference) of the circle
        circle_perimeter = 2 * math.pi * self.radius
        print(f"Perimeter of the circle with radius {self.radius}: {circle_perimeter:.2f}")


my_circle = Circle()


my_circle.area()
my_circle.perimeter()
