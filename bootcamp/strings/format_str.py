#formated strings
first_name = 'john'
last_name = 'smith'
age = 40
print('hello',first_name, last_name, 'your age is', age)
print('hello '+ first_name + ' ' + last_name + ' your age is ' + str(age))
print(f'hello {first_name} {last_name} your age is {age}')

# an fstring can also be stored in a variable
s = f'{2.3 * 4.2 / 5.1:.2f}' # to approximate you just add a colon and the number of decimal places i.e :.2f for 2 decimals, :.3f for three decimal places 
print(s)

#using fstrings to convert from celsius to fahrenheit
#fahrenheit = celsius * 1.8 + 32
celsius = 15.4
print(f"{celsius} degrees celsius = {celsius * 1.8 + 32} degrees fahrenheit")