#WORKING WITH DICTIONARIES 
# dictionary is a mutable data type
# len() can also be used with dictionaries
person = {'name': 'john', 'age': 30, (1, 2, 3): 100}
print(len(person))
# to chnage the name of an element "variable[key] = new_name"
person['name'] ='Dan'
print(person)
# if you want to assign a value to a non existing key the key/value pair can also be added
person['location'] = 'Berlin' # this will add the key and value to the dict person
print(person)
a = person['age'] # we can use key like the way we use index in lists
print(a) #this returns the value in key named 'age'
# however a keyerror will be raised if the key doesnt exist
# we can avoid keyerror by using the getmethod that returns the value associated with the key if the key exist or a default value 
# if only specified and the key doesnt exist
# if the doesnt exist and no dfault value is given it will return none
value = person.get('city', 'key does not exist')
print(value) # key does not exist

value = person.get('name', 'key does not exist')
print(value) # Dan

#pop() this removes the pair and return the value of the specified from the dict
# if the key doesnt exist it returns key KeyError
name = person.pop('name')
print(name, person)

#popitem() it removes and return the last inserted key/value pairs as a tuple
print(person.popitem())

#you can just delete from a dict without returning anything
del person['age']
print(person)
# if the key doesnt exist it will raise an exception KeyError

germany = {
    'cities': ['Hamburg', 'Berlin', 'Munich'],
    'info': {'population': 83_000_000, 'people': ["Einstein", 'Bach', 'Gauss']}
}
print(germany['cities'][1])
print(germany['info']['people'][2])

countries = [
    {
        'cities': ['Hamburg', 'Berlin', 'Munich'],
        'info': {'population': 83_000_000, 'people': ['Einstein', 'Bach', 'Gaus']}
    }
    {
        'cities': ['paris', 'lyon', 'bordeaux'],
        'info': {'population': 67_000_000, 'person': ['Monet', 'Marie Curie', 'Napoleon']}
    }
]

print(countries[0]['cities'])
print(countries[1]['person'][1])