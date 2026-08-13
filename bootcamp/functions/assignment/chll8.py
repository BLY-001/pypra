# Challenge #8
# Change the solution of the previous challenge so that the function receives a string of numbers separated by a comma.
# Example:
# nums = '2, 3, 10, 5'
# print(equilibrium_index(nums)) # => 2
# nums = '3, 3, 10, 5'
# print(equilibrium_index(nums)) # => False

def equilibirum_index(nums):
    x =[int(num.strip()) for num in nums.split(',')]
    for i in range(len(x)):
        if sum(x[:i]) == sum(x[i+1:]):
            return i
    return False    


print(equilibirum_index('2, 3, 10, 5'))