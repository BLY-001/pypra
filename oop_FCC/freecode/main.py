from phone import Phone

item1 = Phone("jabphone", 750, 6)
# item1.__name= "OtherItem"
item1.apply_increment(0.2)
item1.apply_discount()
print(item1.price)

item1.send_email()
