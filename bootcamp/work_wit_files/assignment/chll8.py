# challenge #8
# Write a Python script that compares line by line two text files and displays the lines that differ.

with open('new_file.txt', 'r') as file:
    content = [line.strip() for line in file if line.strip()]
    # filtered = set(content)
    # print(filtered)
with open('nf.txt', 'r') as f:
    k = [line.strip() for line in f if line.strip()]
 
z = zip(content, k)
list_zip = list(z)
i = 0
for item in list_zip:
    i += 1
    if item[0] != item[1]:
        list_item =list(item)
        str_item = '\n'.join(list_item)
        print(f'this happened in line {i}')
        print(str_item)