#DICTIONARY OPERATION AND METHODS
person = {'name': 'John', 'age': 30, 'location': 'USA'}

friend = person # both names reference the same memory address 
person ['name'] = 'peter'
print(friend) # the change will affect both friend and person cos they belong to the same memory address


#to create a copy of a dict use copy()
neighbor = person.copy()
person['location'] = 'Europe'
print(neighbor, person)

#update() this method is also used to extend dict with the items of another dictionary is update()
countries = {'ro': 'Romania', 'US': 'United State of America', 'de': 'Germany'}
countries.update({'hu': 'Hungary', 'fr': 'France'})
print(countries)

# to clear out the dictionary call clear()
person.clear()
print(person, friend)

