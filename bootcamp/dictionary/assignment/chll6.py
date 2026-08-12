# Consider this dictionary. Print a sorted view of the dictionary by the third field of its values, in reverse order.
# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# The output should be: [('Maria', ('Zagreb', 3800, 40)), ('Diana', ('NYC', 3500, 31)), ('John', ('London', 4000, 28))]
# P.S. Do it with a single line of code.

employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
view = sorted(employees.items(), key = lambda items: items[1][2], reverse= True)
print(view)