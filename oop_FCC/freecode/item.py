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
        self.__name = name
        self.__price = price
        self.quantity =quantity

        #Action to execute
        Item.all.append(self) #this append the self object anytime its added

    @property
    def price(self):
        return self.__price

    def apply_increment(self, increment):
        self.__price = self.__price + self.__price * increment

    def apply_discount(self):
            self.__price = self.__price * self.pay_rate # we used self.payrate to access the payrate of 80percent in the class level
        # and also to make it easy to use another payrate for another product by instantiating it it directly from the instance level
        

    @property #this decorator changes object to read only mode, it cannot be changed once the instance is created
    #Property Decorator Read-only Attribute
    def name(self):
        return self.__name #the double underscore avoids changing the name from an instance level

    @name.setter #this decorator is used to change the name of an object even if its in read_only mode
    def name(self, value): 
        if len(value) > 10:
            raise Exception("the name is too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity
    
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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})" # "{self.__class__.__name__} is used instead of item so that the repr can be accessed from an instance level

    def __connect(self, smpt_server):
        ...

    def __prepare_body(self):
        return f"""
        Hello someone
        we have {self.name} {self.quantity} times
        Regards, JimShapedCoding
        """
    def __send(self):
        ...

    def send_email(self):
        self.__connect(" ")
        self.__prepare_body()
        self.__send()