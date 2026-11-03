# Challenge #5
# Change the solution from the previous challenge so that the script that prints out the last n lines of the file refreshes the output every 3 seconds (as the file changes or updates). This is similar to the tail -f Linux command.
import time
def tail(name, num):
    with open(name, 'r') as file:
        content = file.read().splitlines()
        d = '\n'.join(content[-num:])
        return d
while True:
    t = tail('chll2.txt', 5)
    print(t)
    time.sleep(3)