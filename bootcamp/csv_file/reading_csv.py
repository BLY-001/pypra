#READING CSV FILES

import csv
with open("airtravel.csv", "r") as f:
    reader = csv.reader(f) # this is to read the csv file
    #to not display the header of the file we are accessing we use next(reader)
    next(reader) # this will make it skip the first line
#     for row in reader:
#         # print(row) #the rows are printed each in its own list
#         # print(row[1]) # this will print all items at index one of each of the list
    
# # we want to create a dictionary that will contain the year as key and the amount of flights in 1958 as values
    year_1958 = dict() #decalring an empty dict
    for row in reader:
        year_1958[row[0]] = row[1]
    # print(year_1958)
    max_1958 = max(year_1958.values())
    # print(max_1958)
    min_1958 = min(year_1958.values())
    for k, v in year_1958.items():
        if max_1958 == v:
            print(f"Busiest Month in 1958:{k}, flights:{v.strip()}")
        elif min_1958 == v:
            print(f"the minimum value is {v}")