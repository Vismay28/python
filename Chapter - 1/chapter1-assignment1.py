# Assignement: Take diameter as input and calculate the area of a circle

pi = 3.14159
diameter = float(input("Please enter the diameter of the circle: "))
radius = diameter / 2
area = pi * radius * radius
print("The area of the circle with diameter " + str(diameter) + " is: " + str(area))