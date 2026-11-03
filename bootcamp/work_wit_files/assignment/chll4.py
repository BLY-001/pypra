# challenge #4
# Create a Python function called tail that reads the last n lines of a text file. The function has two arguments:
#  the file name and n (the number of lines to read). This is similar to the Linux `tail` command.
#Example: tail('sample_file.txt', 5) will return the last 5 lines from sample_file.txt.
def tail(name, num):
    with open(name, 'r') as file:
        content = file.read().splitlines()
        last = content[-num:]
        my_str = '\n'.join(last)
        return my_str
        

print(tail('chll2.txt', 5))