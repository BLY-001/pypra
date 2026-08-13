# Challenge #5
# Write a Python program that calculates and displays the sum, the product and the average of n float numbers
# entered by the user, each on a separate line. Enter 0 to finish.
count = 0
product = 0
sum = 0
average = 0
# fl_input = float(input("write the float number here: "))
while True:
    fl_input = float(input("write the float number here: "))
    if fl_input == 0:
        break
    count += 1
    if count >= 1:
        product = 1
    product *= fl_input
    sum += fl_input
    if count > 1:
        average = sum/count
print(sum)
print(product)
print(average)

