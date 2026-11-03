#lambda functions
# syntax: lambda input_variable: expression_to_return
lambda_tax = lambda price: price * 0.15
print(lambda_tax(2))

double_espresso_shot = lambda price: price * 2
print(double_espresso_shot(5))

#HIGHER ORDER FUNCTIONS: functions that can take other functions as arguments and also can return a function as output
# 1. map()
menu_prices = [4.50, 3.50, 5.00]
#the updated list will add 0.5 to all the numbers in the list menu_prices
updated_price = list(map(lambda price: price + 0.5, menu_prices))
print(updated_price)

drinks = ['latte', 'espresso', 'mocha']
loud_drinks = list(map(lambda drink: drink.upper(), drinks))
print(loud_drinks)

#2. filter()
menu_items = [{'name':'Espresso', 'price': 3.50},
              {'name':'Latte', 'price': 4.50},
              {'name':'Mocha', 'price': 5.00}
              ]
#this will filtered the list and screen out item with price  greater than 4.50
filtered_menu = list(filter(lambda item: item['price']<=4.50, menu_items))
print(filtered_menu)

prices = [1.50, 5.00, 3.25, 6.00]
cheap_prices = list(filter(lambda price: price < 4.00, prices))
print(cheap_prices)

#3. sorted()
menu_items = [{'name':'Mocha', 'price': 5.00},
              {'name':'Latte', 'price': 4.50},
              {'name':'Espresso', 'price': 3.50}
              ]
#sort based on their price dictionary keys
sorted_by_price = sorted(menu_items, key= lambda x:x['price'])
print(sorted_by_price)

cart = [{'item': 'Cup', 'qty': 10}, {'item': 'Spoon', 'qty': 3}]
sorted_cart =sorted(cart, key= lambda item: item['qty'])
print(sorted_cart)

li = list(map(lambda x: x *2, prices))
l = [x*2 for x in prices]
print(l)
print(li)