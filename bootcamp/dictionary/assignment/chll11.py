# Challenge #11
# Consider the dictionary from the previous challenge.
# Create a new dictionary called profit that stores the profit of the company, if the profit margin is 25% of the sales.
# Use dictionary comprehension if possible.
 jhnb
years = [2015, 2016, 2017, 2018, 2019, 2020]
sales = [350000, 400000, 410000, 439000, 500000, 290000]

z = zip(years, sales)
z_d = dict(z)
new_dict_pr = {k:v *0.25 for k, v in z_d.items()}
print(new_dict_pr)