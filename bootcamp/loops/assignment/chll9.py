# Challenge #9
# Write a Python program that finds the common characters that appear in two given strings.

x = "abdulkrreem"
y = "karimotu"
seen = ""
for n in x:
    if n in y and n not in seen:
        print(n, end = " ")
        seen += n
    