# Let's generalize the last challenge and sort a dictionary by any field of its values if the value is a composite type (list, tuple, etc).
# Example: Considering this dictionary print a sorted view of the dictionary by the second field of its values.
# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# The output should be: [('Diana', ('NYC', 3500, 31)), ('Maria', ('Zagreb', 3800, 40)), ('John', ('London', 4000, 28))]
# P.S. Do it with a single line of code.
employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
view = sorted(employees.items(), key = lambda items: items[1][1])
print(view)