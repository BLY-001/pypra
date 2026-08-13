# list slicing 
numbers =[1, 2, 3, 4, 5]
nums = numbers[1:4]
print(f'nums: {nums}')
print(f'numbers: {numbers}')
print(numbers[:3]) # from start to index 3 excluded
print(numbers[2:]) # from 2 to the end of the string
print(numbers[1:5:3]) # from 1 to 5 excluded using step 3
print(numbers[4:1:-2]) # negative numbers can also be used in slicing where -1 means the last number in the list
# in the case above -2 is the step
print(numbers[::])# this will return the entire list
print(numbers[::-1])# to reverse the list from the back to the front
print(numbers[1:100])# out of bound slices doesnt return error
numbers[0:2] = ['a', 'b'] # slicing can be used to modify a list
print(numbers)
numbers[0:2] = ['x', 'y', 'z']
print(numbers)

print("#" * 10 + " LIST ITERATION " + "#" * 10)
ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']
for ip in ip_list:
    print(f'connecting to {ip} ...')
# to check membership of an item in a list use in
print('10.0.0.1' in ip_list)