# Challenge #9
# Create a Python script that calculates and displays the number of occurrences of each element of a list.
# Sample list: list('mamma mia mm')
# Expected Result:
# m ---> 6
# a ---> 3
# ---> 2
# i ---> 1

sample_list = list("mamma mia mm")
dup = []
for elements in sample_list:
       if elements not in dup:
        dup.append(elements)
        print(f"{elements} ---> {sample_list.count(elements)}")


