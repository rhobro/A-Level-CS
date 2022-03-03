from pygame_functions import *

screenSize(800,800)
setBackgroundColour("darkblue")

setAutoUpdate(False)

class Brick():
    def __init__(self,x,y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.active = True

    def draw(self):
        drawRect(self.x, self.y, self.width, self.height,self.colour)

    def checkHit(self, ball):
        if ball.x > self.x-10 and ball.x < self.x+self.width+10 and ball.y > self.y-10 and ball.y< self.y+self.height+10:
            ball.yspeed *= -1
            if ball.yspeed <0:
                ball.y -=10
            else:
                ball.y +=10
            return True
        return False

    def update(self,balls):
        if self.active:
            self.draw()
            for ball in balls:
                if self.checkHit(ball):
                    self.active = False
                    return


class Ball:
    
    def __init__(self, x, y, xspeed, yspeed):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed

    def draw(self):
        drawEllipse(self.x - 10, self.y - 10, 20, 20, "red")

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed

        if self.x < 0 or self.x > 800:
            self.xspeed *= -1
        if self.y < 0 or self.y > 800:
            self.yspeed *= -1


class Bat(Brick):

    def __init__(self):
        super().__init__(400, 750, 150, 10, "white")
    
    def move(self):
        if keyPressed("right"):
            self.x += 8
        elif keyPressed("left"):
            self.x -= 8
    
    def update(self, balls):
        self.move()
        self.draw()
        for ball in balls:
            self.checkHit(ball)



bricks = []
balls = []
player = Bat()

for x in range(0, 800, 75):
    bricks.append(Brick(x, 150, 70, 50, "green"))
balls.append(Ball(400, 400, 10, -10))


lives = 3
livesLabel = makeLabel("Lives: " + str(lives),20,10,10,"white")
showLabel(livesLabel)
while lives > 0:
    clearShapes()
    for br in bricks:
        br.update(balls)
    for ball in balls:
        ball.move()
        ball.draw()
    player.move()
    player.update(balls)

    updateDisplay()
    tick(60)

endWait()


