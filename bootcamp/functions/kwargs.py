# VARIABLE-LENGTH ARGUMENTS - kwargs

# **kwargs will be used to call the function with a variable number of keyword arguments
# kwargs stands for keyword arguments and it builds a variable length dictionary of key:value pairs.

def my_function(**kwargs):
    print(kwargs) # kwargs is a dictionary so we can iterate on its keys and values
    for k, v in kwargs.items():
        print(f'k is {k} and v is {v}')

my_function(name = 'john', age= 40, location= 'london')
person = {'name':'andreas', 'age': 30, 'location': 'berlin'}
my_function(**person)

# to define a function that can connect to the server using ssh
def connect(ip, port, username, password):
    print(ip, port, username, password)

linux_server = {'ip': '200.0.10.1', 'port': 22, 'username': 'admin', 'password': 'secretPass'}
connect(**linux_server) #this is called dictionary unpacking

# nb : the name *args and **kwargs are just naming conventions u can use any other naming styles as long as you use * for positional arguments and ** for keyword arguments 