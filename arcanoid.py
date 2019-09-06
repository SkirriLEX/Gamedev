import pygame
import time
import math

COLOR_BLACK = ( 0, 0, 0)
COLOR_WHITE = ( 255, 255, 255)
COLOR_GREEN = ( 0, 255, 0)
COLOR_RED = ( 255, 0, 0)
MAP_HEIGT = 500
MAP_WIDTH = 700
BALL_RADIUS = 4

class Point:
    x = 0.0
    y = 0.0
    def __init__  (self,x,y):
        self.x = x
        self.y = y
    def get(self):
        return [self.x,self.y]

class Ball(Point):
    point = Point(0.0,0.0)
    k = 0.0
    speed = 0.0
    def __init__  (self,point:Point,k,speed):
        self.point = point
        self.k = k
        self.speed = speed
    def getCoordinate(self):
        return self.point.get()
    def getNextPoint (self):
        y = 0
        return y 

def vectorCount(A:Point,B:Point):
    S = abs (math.sqrt((B.x-A.x)*(B.x-A.x) + (B.y-A.y)*(B.y-A.y)))
    return S

size = (MAP_WIDTH, MAP_HEIGT)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My firsArcanoid")
carryOn = True
clock = pygame.time.Clock()
pBall = Ball(Point(40,50),0.123,1)
while carryOn:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop

    screen.fill(COLOR_WHITE)

    pygame.draw.circle(screen, COLOR_RED, pBall.getCoordinate(),BALL_RADIUS)

    pygame.display.flip()
    print (vectorCount(Point(0,3),Point(4,0)))
    clock.tick(60)
pygame.quit()
    