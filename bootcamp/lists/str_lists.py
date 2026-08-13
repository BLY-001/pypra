# split() and join()
# split a string into a list and join a list into a string
s1 = "i am learning python programming"
l1 = s1.split()
# we can use other symbols as delimeter to seperate the list by just puting it inside a parenthesisby default it use space as a delimeter
#  
print(l1)

ip_list = ['192.168.0.1', '192.168.0.2', '192.168.0.3']
ip_str = ','.join(ip_list)