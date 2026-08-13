# Challenge #10
# Write a Python script that prompts the user for the radius of a circle and calculates its area. Circle's area = pi * r ** 2 where pi = 3.1415
# Using an f-string display the area of the circle with 4 decimal places.

PI = 3.1415
radius = int(input('write the radius here :'))
print(f'a circle with {radius}m will have an area of {PI * radius ** 2:.4f}m²')