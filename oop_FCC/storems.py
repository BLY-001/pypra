# class Robot:
#     def __init__(self, name, rating, quantity, price):
#         self.name = name
#         self.rating = rating
#         self.quantity = quantity
#         self.price = price
#         self.switch = False
#     def total_price_per_time(self, time):
#         return f"{self.quantity * self.price} in {time}seconds"
#     def __str__(self):
#         return f"the name of the robot is {self.name}"
#     def __mul__(self, other):
#         return self.quantity * other.quantity
#     def turn_on(self):
#         self.switch = True
#         return self.switch
    

# robot1 = Robot('aish', 'A', 2, 300)
# print(robot1)
# print(robot1.rating)
# print(robot1.name)
# print(robot1.total_price_per_time(5))
# print(robot1.turn_on())
# print("____________"* 10)
# robot2 = Robot('kali', 'B', 3, 500)
# print(robot2)
# print(robot2.rating)
# print(robot2.name)
# print(robot2.total_price_per_time(3))
# # print(robot1 * robot2)


class Ecosystem:
    def import_weather(self):
        keyword = "import"
        library_name = "weather_service"
        library = f"{keyword} {library_name}"
        return library
    
    def test_ecosystem():
        eco = Ecosystem()
        return eco.import_weather()

    def solution():
        return test_ecosystem()





