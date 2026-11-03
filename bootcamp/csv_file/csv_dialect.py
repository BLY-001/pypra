#CSV DIALECT

#a dialect describes the properties of a csv file such as delimeter, quoting mechanism, escape character and line terminator
# we can group all properties of a csv file in a custom dialect

import csv

# to see the existing dialects
print(csv.list_dialects())

# we have a file csv file named item.csv that uses "#" character as a delimeter

#to register a dialect 
csv.register_dialect("hashes", delimeter= '#', quoting=csv.QUOTE_NONE, lineterminator="\n")

with open("items.csv", "r") as csvfile:
    reader = csv.reader(csvfile, dialect="hashes")
    for rows in reader:
        print(rows)

# to write to this file you will pass in the dialect to the writer method of the csv module

with open("items.csv", "a") as csvfile:
    writer = csv.writer(csvfile, dialect="hashes")
    writer.writerow(("spoon", 3, 1.5))