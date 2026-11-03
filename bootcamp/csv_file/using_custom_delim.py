#USING CUSTOM DELIMITERS INSTEAD OF COMMA

import csv

with open ("passwd", 'r') as f:
    reader = csv.reader(f, delimiter= ":", lineterminator= "\n")
    for rows in reader:
        print(rows)