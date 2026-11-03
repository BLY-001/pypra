# Challenge #2
# Change the solution from the previous challenge and use : (colon) as the delimiter.
# Are you stuck? Do you want to see the solution to this exercise? Click here.

import csv

people = [
['Dan', 34, 'Bucharest'],
['Andrei',21, 'London'],
['Maria', 45, 'Paris']
]
csv.register_dialect("hashes", delimiter="#", lineterminator="\n")
with open ("people1.csv", "w") as f:
    writer = csv.writer(f, dialect="hashes")
    for items in people:
        writer.writerow(items)
        

with open("people1.csv", "r") as f:
    reader = csv.reader(f)
    print(list(reader))
    