class Microwave:
    def __init__(self, brand:str, power_rating:str, price): #initializer this takes care of initializing the class, this means if you hve any additional info u want to give the class when you are creating an instance
        #the code will be run here as soon as u instantiate it
        self.brand = brand
        self.power_rating = power_rating
        self.price = price
        self.turned_on = False
        #self is the actual instance of the class
    def turn_on(self):
        if self.turned_on:
            print(f"microwave({self.brand}) is already turned on")
        else:
            self.turned_on = True
            print(f"microwave ({self.brand}) is now turned on")
    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"microwave({self.brand}) is now switched off")
        else:
            print(f"microwave ({self.brand}) is already turned off")
           
    def run(self, seconds):
        if self.turned_on:
            print(f"Running ({self.brand}) for {seconds} seconds")
        else:
            print(f"A mystical force whispers: 'turn on your microwave first...'" )

    def __add__(self, other):
        return f"{self.price + other.price} "
    def __str__(self):
        return f"mircowave: {self.brand}, power_rating({self.power_rating}), price({self.price})"
    def __repr__(self):
        return f"insha allah (microwave: {self.brand}, power_rating --> {self.power_rating}, price -->{self.price})"
    


smeg = Microwave("smeg", "B", 3 ) #the colon and Microwave aftert the instance name "smeg" is just a type annotation you can ignore it an use it normally i.e smeg = Microwave()
meg = Microwave("meg", "A", 2)
smeg.turn_on()
smeg.run(10)
smeg.turn_off()
print(meg + smeg)
print(meg)
print(repr(smeg))