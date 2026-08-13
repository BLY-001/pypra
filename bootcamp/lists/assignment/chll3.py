# Challenge #3
# Consider the following string: nums = '10,20,30,40,50'
# Create a Python script that creates a list of integers from the string.
# The resulting list will be: [10, 20, 30, 40, 50]

nums = "10,20,30,40,50"
num_list = nums.split(',')
num_g = [int(c) for c in num_list]
print(num_g)

real_number = list()
for item in num_list:
    real_number.append(int(item))
print(real_number)

