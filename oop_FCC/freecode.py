import csv #this is needed because of the csv file we are using
class Item:
    #Class attributes is an atribute that belong to the class itself nd can also be assessed from the instance level
    pay_rate = 0.8 # the pay rate after 20% discount
    #we can also assign to each parameter the ind of data types the will be by writing parameter:data type
    all = [] #we want to create an empty list where we can add all our instances to
    def __init__(self, name:str, price:int, quantity=0): #if we did not pass any value for quantity we want it to hve a default value of 0
        #run validations to the received arguments, this raises an exception if the assertion is not met
        #you can also print an error message once the assertion is being raised using comma after the assertion and an f"string"
        assert price >= 0, f"price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"quantity{quantity} is not greater than or equal to zero!"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity =quantity

        #Action to execute
        Item.all.append(self) #this append the self object anytime its added

    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate # we used self.payrate to access the payrate of 80percent in the class level
    # and also to make it easy to use another payrate for another product by instantiating it it directly from the instance level
    @classmethod #this is a decorator that changes the behaviour of objects  below to a class method it takes a class object as its only parameter 
    def instantiate_from_csv(cls):
        with open("input.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Item(
                    name=item.get("name"),
                    price=float(item.get("price")),
                    quantity=int(item.get("quantity")),
                )

    @staticmethod # this is a decorator that changes the behaviour of the block below to a static method it takes normal parameter like a normal function
    def is_integer(num):
        # we will count out the float that are point zero
        # for i.e: 5.0, 10.0
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer() #this returns only float that are integer
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})" # "{self.__class__.__name__} is used instead of item so that the repr can be accessed from an instance level

    
class Phone(Item): #class Phone is a child of the item class and it inherits from it 
    def __init__(self, name:str, price:int, quantity=0, broken_phone=0): 
            #Call to super function to have access to all attribute/methods
            super().__init__(
                name, price, quantity
            ) #this allows us to access all the attribute of the parent class  

            #run validation of the received argument    
            assert broken_phone >= 0, f"broken_phone{broken_phone} is not greater than or equal to zero!"
    
            #Assign to self object
            self.broken_phone= broken_phone
    










phone1 = Phone("jscPhonev10", 500, 5, 1,)
# phone2 = Phone("jscPhonev20", 700, 5, 1)
print(Phone.all)
print(Item.all)



# Item.instantiate_from_csv()
# print(Item.is_integer(3))


# item2.pay_rate = 0.7 # we are setting the pay rate of item2 to 0.7 from the instance level
# item2.apply_discount()
# item1.apply_discount()
# print(item1.price)
# print(item2.price)


#to check all the attributes under a specific object use object.__dict__
# print(Item.__dict__) #CLASS LEVEL ATTRIBUTES
# print(item1.__dict__) #INSTANCE LEVEL ATTRIBUTES

# print(item1.quantity)
# print(item1.calculate_total_price())
