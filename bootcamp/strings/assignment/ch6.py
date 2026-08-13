# Write a Python script to get a string made of the first and the last 2 chars from a given string entered by the user.
# Sample String: 'Hello!'
# Expected Result: 'Heo!'

chy = 'Hello!'
chy = chy[:2] + chy[-2:]
print(chy)