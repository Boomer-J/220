"""
name: Jenks, Boomer
bumper.py

Problem: write a program that simulates bumper cars in graphics window using the graphics lib

Certification of authenticity:
I certify that this assignment is entirely my own work.
"""
from math import *
import random
from graphics import *

W = 300
H = 300
carList = []

def bumper(win, carList):
    for step in range( 200 ):
        for i in range(len(carList)):
            c, dx, dy = carList[i]
            x = c.getCenter().getX()
            y = c.getCenter().getY()
            r = c.getRadius()

            if (x  <= 0 + r ) or (x >= W - r):
                dx = -dx
            if (y <= 0 + r) or(y >= H - r):
                dy = -dy


            (boolVal, car1, car2) = hasCollided(carList)
            if boolVal == True:
                c1, dx1, dy1 = car1
                c2, dx2, dy2 = car2

                for list in carList:
                    if car1[0] in list:
                        list.pop(1)
                        list.insert(1, dx1)
                        list.pop(2)
                        list.insert(2, dy1)
                    if car2[0] in list:
                        list.pop(1)
                        list.insert(1, dx2)
                        list.pop(2)
                        list.insert(2, dy2)
                c1.move(dx1, dy1)
                c2.move(dx2, dy2)

            else:
                c.move(dx, dy)
                carList[ i ] = [ c, dx, dy ]


def hasCollided(carList):
    newcarList = []
    for i in range(len(carList)-1):
        for j in range(i+1, len(carList)):
            c1 = carList[i][0]
            c2 = carList[j][0]

            dx1 = carList[i][1]
            dy1 = carList[i][2]
            dx2 = carList[j][1]
            dy2 = carList[j][2]

            r1 = c1.getRadius()
            r2 = c2.getRadius()

            P1 = Point(c1.getCenter().getX(), c1.getCenter().getY())
            P2 = Point(c2.getCenter().getX(), c2.getCenter().getY())
            dist = distance(P1, P2)
            if (dist < (r1 + r2)):
                if isSameSign(dx1, dx2):
                    dx1 = -dx1
                elif isSameSign(dy1, dy2):
                    dy1 = -dy1
                else:
                    dx1 = -dx1
                    dy1 = -dy1
                    dx2 = -dx2
                    dy2 = -dy2
                while (dist <= (r1 + r2)):
                    c1.move(dx1, dy1)
                    c2.move(dx2, dy2)
                    P1 = Point(c1.getCenter().getX(), c1.getCenter().getY())
                    P2 = Point(c2.getCenter().getX(), c2.getCenter().getY())
                    dist = distance(P1, P2)

                newcarList.append([c1, dx1, dy1])
                newcarList.append([c2, dx2, dy2])
                return True, newcarList[0], newcarList[1]
    return False, 0, 0

def distance(P1, P2):
    return sqrt( pow( P1.getX() - P2.getX(), 2 ) + pow( P1.getY() - P2.getY(), 2 ))

def isSameSign(a, b):
    if ((a < 0) and (b < 0)) or ((a > 0) and (b > 0)):
        return True

def isInBounds(c1, c2):
    boundsList = []
    boundsList.append(c1)
    boundsList.append(c2)
    for i in range(len(boundsList)):
        r = boundsList[i].getRadius()
        x = boundsList[i].getCenter().getX()
        y = boundsList[i].getCenter().getY()
        if ((x  <= 0 + r ) or (x >= W - r)) or ((y <= 0 + r) or(y >= H - r)):
            return False
        return True


def end(win):
    waitForClick( win, "Click to End" )
    win.close()


def waitForClick( win, message ):
    message = "Hello Welcome to Bumper Cars!"

    startMsg = Text( Point( win.getWidth()/2, win.getHeight()/2 ), message )
    startMsg.draw( win )
    win.getMouse()
    startMsg.undraw()

#----------------------------------------------------------------
def main():
    win = GraphWin( "Bumper Cars!", W, H )
    carColor = ["red", "blue", "pink", "purple", "green"]
    for i in range(5):
        c = Circle( Point( random.randrange( 16, W-15, 20 ), random.randrange( int(H/3), int(2*H/3), 20 ) ), 10)
        c.setFill(carColor[i%len(carColor)])
        c.draw(win)
        carList.append([c, 7 - random.randrange(10), 7 - random.randrange(10)])




    waitForClick( win, "Click to Start" )

    bumper(win, carList)
    end(win)

main()
