# THE WITH STATEMENT
#always remember to close your file whenever you are done working
#however you can close your file by calling the close function when you are done
# or simply you can just use the with statement, it automatically close the file once you are out of it
with open('configuration.txt') as file:
    content= file.read()
    print(content)

# the file will be open inside the statement and closed outside it
print(file.closed) #the method inside print returns true if the file is closed and false otherwise  