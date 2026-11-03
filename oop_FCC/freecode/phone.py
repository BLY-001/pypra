from item import Item


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