#bouncing ball 1

#this demonstrates the use of variables to model a bouncing ball

from pygame_functions import *

screenSize(600,600,400,100)
setBackgroundColour("white")
setAutoUpdate(False)


ballx = 100
bally = 50
ballradius=20
ballspeed=0


running = True
while running:
    clearShapes()
    drawEllipse(ballx,bally,ballradius*2,ballradius*2,"red")
    ballspeed = ballspeed + 1
    bally = bally + ballspeed
    
    if bally > 600 - ballradius:
        ballspeed = int(0-ballspeed*0.90)
        bally=600-ballradius
    updateDisplay()
    tick(30)
endWait()


