#bouncing ball 3

#In this version, we create an object class called Ball

from pygame import math
from pygame_functions import *
import random as rand

screenSize(600,600,400,100)
setBackgroundColour("white")
setAutoUpdate(False)

class Ball():
    def __init__(self,x,y,radius,speed, colour):  # the __init__ method is called whenever the object is		
        self.x = x                                 #created (or "initialised")
        self.y = y
        self.radius = radius      # we store the variables that describe the ball
                                  # (called the PROPERTIES)
        self.speed = speed        # using the self keyword to indicate that they
        self.colour = colour      # belong to this object

    def draw(self):               #we also create METHODS that do things with the object
        drawEllipse(self.x,self.y,self.radius*2,self.radius*2,self.colour,0)

    def move(self):               # This method is used to adjust the position of the ball
        self.y += self.speed


    def checkBounce(self):        #this method checks to see if the ball should bounce
        if self.y >= 600-self.radius:  # and adjusts the speed if necessary
            self.y = 600-self.radius
            self.speed = int(0- self.speed * 0.90)
        else:
            self.speed+=1         #otherwise, it accelerates downwards due to gravity



#now we just create two balls. They have different names and are created from the Ball template
smallBall = Ball(100,0,20,0,"red")  # we do this by sending the important properties to the __init__ method of
                               # each new ball object

largeBall = Ball(200, 50, 40,5, "green")  #notice that this ball has different properties to the smallBall

balls = []
for i in range(10000):
    r = rand.randint(10, 20)
    x = rand.randint(r, 600-r)
    y = rand.randint(r, 600-r)
    v = rand.randint(0, 10)
    balls.append(Ball(x, y, r, v, rand.choice(["red", "green", "yellow", "purple", "orange"])))

running = True
while running:
    clearShapes()
    for b in balls:
        b.move()
        b.checkBounce()
        b.draw()
    updateDisplay()
    tick(30)
endWait()



