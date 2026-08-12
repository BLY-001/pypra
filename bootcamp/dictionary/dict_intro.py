#DICTIONARIES IN PYTHON
#Dictionaries are everywhere.
# modules, classes, objects, and sets are all implemented internally as dictionaries
#  a dictionary is an ordered collection of keys:value pairs, separated by commas and enclosed by curly braces.
person = {'name': 'john', 'age': 30, 10:('a', 'b')}
print(type(person))
# compared to list sets and tuples dictionary allows us to group together related pieces of information
d1 = dict() #empty dict
d2 = {} #empty dict
#values can be any python data type but the key must be immutable data type i.e strings, integer, tuple, frozenset
#keys are unique and immutable
person = {'name': 'john', 'age': 30, 10:('a', 'b'), "age": 30}if a key appears more than once in a dict only one of it will be used 