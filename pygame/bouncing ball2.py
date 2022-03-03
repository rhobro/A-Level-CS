#bouncing ball 2

#What happens if we need 2 balls?

from pygame_functions import *

screenSize(600,600,400,100)
setBackgroundColour("white")
setAutoUpdate(False)

ball1x = 100
ball1y = 50
ball1radius=40       
ball1speed=0  
ball1Colour = "red"

ball2x = 200
ball2y = 100
ball2radius=60
ball2speed=4  
ball2Colour = "green"


running = True
while running:
    clearShapes()
    drawEllipse(ball1x,ball1y,ball1radius,ball1radius,"red")       #we draw both balls separately
    drawEllipse(ball2x,ball2y,ball2radius,ball2radius,"green")
    
    ball1speed = ball1speed + 1			#we must remember to update their speed individually
    ball2speed = ball2speed + 1
    
    ball1y = ball1y + ball1speed		#we must remember to add the speed to the position each time
    ball2y = ball2y + ball2speed
    
    if ball1y > 600-ball1radius/2:
        ball1speed = int(0-ball1speed * 0.90)
        ball1y=600-ball1radius/2
        
    if ball2y > 600-ball2radius/2:					#each ball must be checked to see if it has reached the bottom of the screen
        ball2speed = int(0-ball2speed * 0.90)
        ball2y=600-ball2radius/2
        
    updateDisplay()
    tick(30)
endWait()

