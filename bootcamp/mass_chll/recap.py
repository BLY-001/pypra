# challenge #1
# Consider the following string declaration which is part of the output of a Linux command.
# my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
# Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.
# Try to solve the challenge in more than one way.

# my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
# print(my_str[32:])
# print(my_str[-17:])

# # Challenge #2
# # Display the following strings literally:
# # It displayed: "You've got an error!"
# # \n means a new line.
# # \ is known as the escape character.
# # Are you stuck? Do you want to see the solution to this exercise? Click here.

# print("""it displayed: "you've got an error!"\n\\n means a new line.\n\\ is known as the escape character""")

# # Challenge #3
# # Write a Python script that converts foot [ft] to centimeter [cm]. 1 ft = 30.48 cm
# # The user will be prompted to enter the value in ft.
# # Display the value in cm with 2 decimals, formatted using an f-string.

# ft = int(input())
# cm = ft * 30.48
# print(f"{ft}ft is equal to {ft * 30.48}cm")

# m = 'mallam'
# if m.strip().lower() == m[::-1]:
#     print("m is a palindrome")

# 
# 
sample = "Hello!"
print(sample[:2] + sample[-2:])

# Challenge #7
# Write a Python program to get a string from a given string where all occurrences of its first character have been changed to '$', except the first character itself.
# Sample String: 'mama'
# Expected Result: 'ma$a'

x ="mama"
y = x[0]
w = x[1:]
z = w.replace("m", "$")
print(y + z)


#
# n = int(input())
m ="sandsjkf" 
# c = m[:n]
# d = m[n+1:]
# f = c + d
# print(f)

the_rest =m[::2]
print(the_rest)

# Challenge #10
# Write a Python script that prompts the user for the radius of a circle and calculates its area. Circle's area = pi * r ** 2 where pi = 3.1415
# Using an f-string display the area of the circle with 4 decimal places.
# Are you stuck? Do you want to see the solution to this exercise? Click here.

# radius = int(input('input a number:'))
# pi = 3.142
# area = pi *radius **2
# print(f'the area of the circle is :{area:.4f} ')

# Challenge #11
# Write a Python script that finds all occurrences of a substring in a given string by ignoring the letter case.
# Are you stuck? Do you want to see the solution to this exercise? Click here.

# m = int(input())
# print(f" european format = {m:,}")

# # Challenge #1
# Create a Python script that asks the user for a number and then prints out a list of all 
# the divisors of each number less than the asked number.
# Are you stuck? Do you want to see the solution to this exercise? Click here.

# m = int(input("input your number: "))
# for n in range(1, m):
#     if m % n == 0:
#         print(n, end= "")

# Challenge #2
# Write a Python program to check if an integer (x) is the power of another integer (y). Prompt the user to input both integers.
# Input: 16, 2
# Output: 2 ** 4 = 16
# Are you stuck? Do you want to see the solution to this exercise? Click here

# x = int(input("input your number: "))
# y = int(input("input the second number: "))

# for n in range(x):
#     if y ** n == x:
#         print(f"{y} ** {n}= {x}") 


# Challenge #3
# Write a Python program that counts and displays the vowels of a given string ignoring the letter case.
# Input str: Hello Everybody!
# Output: 5

# m = input("write your : ")
# vowel = "aeiou"
# x = ""
# count = 0

# for n in m.lower():
#     if n in vowel:
#         x += n
#         count += 1
# print(x, count)

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
# Are you stuck? Do you want to see the solution to this exercise? Click here.

# x, y, z = int(input("input x: ")), int(input("input y: ")), int(input("input z: "))

# if x == y and x == z:
#     print("equilateral triangle")
# elif x == y and y != z:
#     print("isosceles triangle")
# else:
#     print("scalene triangle")

# challenge #5
# Write a Python program that calculates and displays the sum, the product and 
# the average of n float numbers entered by the user, each on a separate line. Enter 0 to finish.
# Are you stuck? Do you want to see the solution to this exercise? Click here.
# sum = 0
# product = 0
# count = 0
# average = 0
# while True:
#     m = float(input("input your float"))
#     if m == 0:
#         break
#     count += 1
#     if count == 1:
#         product = 1 
#     if count >= 1:
#         sum += m
#         product *= m
#         average = sum/count
# print(f"product: {product}, sum: {sum}, average: {average}")

# Challenge #6
# Given the string s1, write a program to return 
# the sum and the average of the digits that appear in the string, ignoring all other characters.
# Input: Python31py50
# Output: Sum: 9, Average: 2.25
# inut = "Python31py50"
# x = 0
# count = 0

# for n in inut:
#     if n.isdigit() == True:
#         count +=1
#         x += int(n)
# average = x/count
# print(x)
# print(average)
#         # print(f"average : {sum(int(n))/ count(n)}") 
   
# input = int(input())
# for n in range(1,11):
#     print(f"{input} * {n} = {input * n}")      

# Challenge #8
# Write a Python script that displays the following pattern from 1 to n where n is entered by the user.
# If the user enters 6 it will display:

# input = int(input())
# for n in range(1, input+1):
#     print(n * str(n))

# challenge #9
# Write a Python program that finds the common characters that appear in two given strings.
# Are you stuck? Do you want to see the solution to this exercise? Click here.

# x = input()
# y = input()

# for items in y:
#     if items in x:
#         print(items, end="")


# Challenge #10
# Write a Python program that iterates over the integers from 1 to 50.
# For multiples of three print "Foo" instead of the number and for multiples of five print "Bar".
# For numbers that are multiples of both three and five print "FooBar".
# for items in range(1, 51):
#     if items % 3 == 0 and items % 3 == 0:
#         print("FooBar")
#     elif items % 3 == 0:
#         print("Foo")
#     elif items % 5 == 0:
#         print("Bar")

# Challenge #11
# Write a Python script that prints out the Fibonacci series up to a given number n.
# Fibonacci Series: https://www.mathsisfun.com/numbers/fibonacci-sequence.html
# Example: if n is 23 it will print out 0, 1, 1, 2, 3, 5, 8, 13, 21
# Are you stuck? Do you want to see the solution to this exercise? Click here.

# n = int(input())
# a = 0
# b = 1
# c =[]
# while a < n:
#     c.append(str(a))
#     a,b =b,a+b
# d =", ".join(c)
# print(d)


# Challenge #12
# Write a Python script that draws the following pattern using for loops.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# secan = 5
# count = 0
# while count < 5:
#     count += 1
#     print(f"{"* " * count}\n")
#     while count == 5 and secan >= 0:
#         secan -= 1
        # print(f"{"* " * secan}\n")
        
# ipv4 = 2**32
# print(len(str(ipv4)))

# laptop = {"brand":"dell", "price": 3000, "RAM": 2}
# laptop.update({"storage":3, "processor": "4mgh"})
# laptop["part"]="mouse" 
# laptop = {**laptop, "jargon":"wire"}
# print(laptop)

# product = {"name": "steph", "cost": 50, "supplier": "josh"}
# c = product["cost"] * 15/100
# fee = format(c, ".2f")
# print(float(fee))

data_list = [11, 3.5, "water", (1, 2)]
# list(data_list[3])
# conv =[str(item) for item in data_list[3]]
# "".join(conv)
# print(conv1)
# result_var = ""
# for item in data_list:
#     result_var+= str(item)
# print(result_var)

# x = str(data_list[0])+str(data_list[1])+ data_list[2] + str(data_list[3][0]) + str(data_list[3][1])
# print(x)

# countries = ["nigeria", "ghana", "niger", "chad", "cameroon"]
# # countries[2:-1]
# print(countries[2:-1])

# number_sequence = list(range(-15,10,4))
# print(number_sequence)

# months = ["january", "february", "april"]
# months.insert(2, "march")
# print(months)

# 
# group_a ={"a", "b", "c", 2, 1, 3}
# group_b = {1,2,3, "g", "f"}
# inter = group_a.intersection(group_b)
# print(list(inter))

# a = [111, 222, 333, 444, 111]
# b = [333, 111, 555, 777, 555]
# c = set(a).union(set(b))
# print(c)

# my_str = 'eth0 Link encap:Ethernet HWaddr00:11:22:33:44:55'
# nl=my_str.split()
# print(nl[0] + nl[-1])

# def calculate_sum(num):
#     a = str(num) * 1
#     b = str(num) * 2
#     c = str(num) * 3
#     d = int(a) + int(b) + int(c)
#     return d

# print(calculate_sum(4))

# mac = ['b4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3', 'a4:6d:83:77:85:f4', 'c4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3']
# mac_u = []
# for element in mac:
#     if element not in mac_u:
#         mac_u.append(element)
# print(mac_u)

# mac_y = list()
# mac_x= [mac_y.append(items) for items in mac if items not in mac_y]
# print(mac_y)

# years = [2010, 2010, 2011, 2011, 2012]
# uni_y = []
# [uni_y.append(item) for item in years if item not in uni_y]
# print(uni_y)

# words = ["anna", "car", "civic", "screen", "level", "cat", "mom"]
# pal = []
# [pal.append(item) for item in words if item == item[::-1]]
# print(pal)

# def reverse(my_string):
#     """ this function takes a string and reverses it"""
#     n_string = my_string[::-1]
#     return n_string

# print(reverse("Beautiful"))

# def remove_from_list(my_list, item):
#     """ this function removes all occurences of a duplicate value"""
#     while item in my_list:
#         my_list.remove(item)
#         if item not in my_list:
#                 return my_list

# print(remove_from_list([1, 2, 1, 1, 1, 1, 3 ], 1))

# def vowel_count(my_str):
#     """this function writes out the appearance of a letter 
#     and its frequency as a key and value"""
#     dicta = {}
#     vowel = "aeiou"
#     for items in my_str.lower():
#         if items in vowel:
#             dicta[items] = dicta.get(items, 0)+ 1
#     return dicta  

# a = vowel_count("Awesome")
# b = vowel_count("Wow! Python is great!") 
# print(b) 

# items = ["apple", 'banana', 'orange', 'apple', 'grape', 'banana', 'mango', 'orange', 'pearl']
# print(sorted(set(items)))

# with open("show_arp.txt", "r") as file:
#     content = file.read().splitlines()
#     r_con = content[1:]
#     em_list = []
#     for items in r_con:
#         s_list = items.split()
#         d = s_list[1], s_list[3]
#         em_list.append(d)
#     print(em_list)    


# area = lambda x: x**2
# print(area(2.5))

# PI = 3.141592653589793
# a = float(format(PI, ".5f"))
# print(a)

# countries = {"USA":"United States of America", "BR":"Brazil", "RS":"Russian", "NGA":"Nigeria", "ARG": "Argentina"}
# s_con = sorted(countries)
# for item in s_con:
#     print(countries[item])

# names = {"John":50000, "Anne":66000, "Tayo":40000, "Pep":300000}
# taxified = map(lambda items: items[1] * 0.1, names.items())
# nama = list(names.keys())
# z = zip(nama, taxified)
# impl = dict(z)
# print(impl)
# taxes = {k:v*0.1 for k, v in names.items()}
# print(taxes)

# f = open("a.txt", "r")
# f.seek(4)
# word = f.read(5)
# print(word)
# f.close()
# print(f.closed)

# with open("a.txt", "a") as file:
#     file.write("May 25:8800\n")

