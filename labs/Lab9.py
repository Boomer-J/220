"""
Name: <Boomer Jenks>
<lab9>.py
"""
from graphics import *
import math
def addTens(x):
    for i in range(len(x)):
        x[i] = x[i]+10

def squareEach(x):
    for i in range(len(x)):
        x[i] = x[i] ** 2

def sumList(x):
    acc = 0
    for i in range(len(x)):
        acc = acc + x[i]
    return acc

def twoNumbers(x):
    for i in range(len(x)):
        x[i] = float(x[i])

def writeSumOfSquares():
    ifn = input("input the file you would like to open: ")
    infile = open(ifn, "r")
    outfile = open("output.txt", "w+")
    for line in infile:
        number = line.split()
        twoNumbers(number)
        squareEach(number)
        s = sumList(number)
        outfile.write("the Sum is:" + str(s) + "\n")


def starter():
    weight = eval(input("what is your weight?: "))
    wins = eval(input("how many wins do you have?: "))
    if weight >= 150 and weight < 160 and wins >= 5:
        print("this individual should be a starter. ")
    elif weight > 199 and wins > 20:
        print("this individual should be a starter. ")
    else:
        print("this individual should not be a starter. ")

def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("Its a leap year!")
    else:
        print("Sadly it's not a leap year ")

def circleOverlap():
    win = GraphWin("Circle Overlap", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt((p1.getX()-p2.getX()) ** 2 + (p1.getY()-p2.getY()) ** 2)
    circle = Circle(p1, radius1)
    circle.draw(win)
    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    circle = Circle(p3, radius2)
    circle.draw(win)
    distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
    if distance <= (radius1 + radius2):
        inst_pt = Point(400 / 2, 300)
        instructions = Text(inst_pt, "These Circles Overlap!")
        instructions.draw(win)
    else:
        inst_pt = Point(400 / 2, 300)
        instructions = Text(inst_pt, "These Circles Don't Overlap")
        instructions.draw(win)
    win.getMouse()
    win.close()






def main():
    circleOverlap()
    leapYear(year=2100)
    starter()
    x = [5, 2, -3]
    addTens(x)
    print(x)

    pass


main()