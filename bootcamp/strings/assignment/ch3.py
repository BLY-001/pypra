# Challenge #3
# Write a Python script that converts foot [ft] to centimeter [cm]. 1 ft = 30.48 cm
# The user will be prompted to enter the value in ft.
# Display the value in cm with 2 decimals, formatted using an f-string.

foot = float(input("enter the foot value:"))
print(f'{foot}ft is equal to {30.48 * foot:.2f}cm')