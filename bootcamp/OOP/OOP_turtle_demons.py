#OOP DEMO: THE TURTLE
#turtle is a popular way for introducing programming to kids.
# imagine a robotic turtle atarting at (0,0) in the x-y plane.after an import turtle, give it the command turtle.forward(15), and 
# it moves (on screen!) 15 pixels in the direction it is facing , drawing a line as it moves.
# give it the command turtle.right(25), and it rotates in-place 25 degrees clockwise.

from turtle import Turtle, Screen #class names use pascal notation

my_screen = Screen() #my_screen is an object of the class screen() used for the canvas
donatello = Turtle() #donatello is an object of class turtle() 
my_screen.canvwidth #the width of the canvas (in pixel)
# attributes of objects are usually changed by calling a method
donatello.shape('turtle') #this changes the shape of donatello to turtle shape
donatello.color('purple') # changes donatello to purple color
donatello.forward(100) # donattello moves 100 pixel in the direction its facing
donatello.right(90)# donatello rotates 90 degrees to the right
donatello.forward(100) # 100 pixel forward
donatello.right(90)# donatello rotates 90 degrees to the right
donatello.forward(100) # donattello moves 100 pixel in the direction its facing
donatello.right(90) # donatello rotates 90 degrees
donatello.forward(200) #200 pixel forward
donatello.home()#returns donattello the starting point
raphael = Turtle() # create another object of the turtle class called raphael
raphael.color('red')
raphael.shape('turtle')
raphael.penup() # pen up so that any line would be written on the screen
raphael.goto(-150, 200) # this moves the turtle(pen) to dimension
raphael.pendown() #pen down so that we can draw new things on the screen
raphael.pencolor('blue')

#we want to loop such that both will draw a circle
# a circle
x = 10
while x <= 50:
   raphael.circle(x) # this will draw a circle of radius of x pixels
   donatello.circle(x + 5) # radius x+5
   x += 10

my_screen.exitonclick()

#Abstraction is a key concept in OOP, and its goal is to handle complexity
#by hiding unnecessary details from the user

#Encapsulation is a mechanism of binding attributes and methods as a single unit
#Encapsulation is also known as data hiding