#FOR LOOPS

# for letter in "python":
#     print(letter)
#     print('bye')
# print('#############')

my_str = input("write anything you like:").lower()
vowels = "aeiou"
for items in my_str:
    if items in vowels:
        print(items, end=" ")

# lesson 2 on debuging

for n in [1,2,3,4,5,6,7]:
    nn = n ** 2
    if nn % 2 == 0:
        print("the number is even")
    else:
        print('number is odd')
