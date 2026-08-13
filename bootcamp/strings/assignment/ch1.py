#Challenge #1
# Consider the following string declaration which is part of the output of a Linux command.
# my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
# Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.
# Try to solve the challenge in more than one way.

my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:fh3'
print(my_str[-18:])
print(my_str[32:])