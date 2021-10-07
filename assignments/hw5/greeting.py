"""
name: Jenks, Boomer
greeting.py

Problem: Create a greeting card in python graphics that creates a heart with
a moving arrow using a loop function.

Certification of authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

win = GraphWin('Circle', 400, 400)
win.setBackground('white')
win.setCoords(10, 10, 20, 20)

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

# arrow
head1 = Point(11.97, 18.53)
head2 = Point(12.08, 18.14)
head3 = Point(11.52, 18.24)
arrow = Line(Point(10.1, 19.87), Point(11.77, 18.37))
arrow2 = Polygon(head1, head2, head3)
arrow2.setFill("black")
arrow.draw(win)
arrow2.draw(win)
for i in range(20, 20):
    arrow.move(10, 10)


coordinate = win.checkMouse()
while coordinate == None:
    coordinate = win.checkMouse()
    print(coordinate)


win.getMouse()
win.close()


