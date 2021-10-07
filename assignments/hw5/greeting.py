"""
name: Jenks, Boomer
greeting.py

Problem: Create a greeting card in python graphics that creates a heart with
a moving arrow using a loop function.

Certification of authenticity:
I certify that this assignment is entirely my own work.
"""
import time
from graphics import GraphWin, Circle, Point, Line, Polygon, Text

win = GraphWin('Circle', 400, 400)
win.setBackground('white')
win.setCoords(10, 10, 20, 20)

# arrow
head1 = Point(12.431077694235588, 18.646616541353385)
head2 = Point(12.406015037593985, 18.145363408521302)
head3 = Point(11.779448621553884, 18.170426065162907)
arrow = Line(Point(10.1, 19.87), Point(12.130325814536342, 18.345864661654137))
arrow2 = Polygon(head1, head2, head3)
arrow2.setFill("black")
arrow.draw(win)
arrow2.draw(win)


# diamond
p1 = Point(12.75, 15)
p2 = Point(15.18, 12.05)
p3 = Point(17.5, 15)
p4 = Point(15.18, 16.2)
dia = Polygon(p1, p2, p3, p4)
dia.setFill('red')
dia.setOutline('red')
dia.draw(win)

# circle 1
cir = Circle(Point(14, 15.87), 1.5)
cir.setFill('red')
cir.setOutline('red')
cir.draw(win)
# circle 2
cir2 = Circle(Point(16.29, 15.87), 1.5)
cir2.setFill('red')
cir2.setOutline('red')
cir2.draw(win)
# diamond 2
p1 = Point(12.75, 15)
p2 = Point(15.18, 12.05)
dia = Polygon(p1, p2, )
dia.setFill('red')
dia.setOutline('pink')
dia.draw(win)

inst_point = Point(15.18, 16)
inst_point2 = Point(15.18, 15)

instructions = Text(inst_point, "Happy")
instructions2 = Text(inst_point2, "Birthday!")
instructions.draw(win)
instructions2.draw(win)

# arrow loop
for i in range(1, 9):
    arrow.move(.5, -.5)
    arrow2.move(.5, -.5)
    time.sleep(1)

win.getMouse()
win.close()
