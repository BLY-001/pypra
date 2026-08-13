# Challenge #4
# Write a Python script that checks if a triangle is equilateral, isosceles or scalene.
# The user will be prompted for the triangle sides.
# Note:
# An equilateral triangle is a triangle in which all three sides have the same length.
# An isosceles triangle is a triangle that has two equal sides.
# A scalene triangle is a triangle that has three unequal sides.
# Input: Enter the lengths of the triangle sides:
# x: 6
# y: 8
# z: 12
# Expected Output: Scalene triangle.

x, y, z = int(input("input x : ")), int(input("input y : ")), int(input("input z : "))
if x ==y and x == z:
    print("the triangle is an equilateral triangle")
elif x != y and x != z and y != z:
    print("this is a scalene triangle")
else:
    print("this is aan isoceless triangle")