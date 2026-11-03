# Challenge #
# Consider this text file that contains multiple duplicate MAC addresses.
# Create a new file that contains only unique MAC addresses. Each MAC should be on its own line.


#VERY SHORT SOLUTION 2
with open("mac.txt", 'r') as f:
    unique = set(line.strip() for line in f if line.strip())
with open('nf.txt', 'w') as d:
    for mac in sorted(unique):
        d.write(mac + '\n')
print(filtered_list)