from graphics import *
from random import randrange
from button import Button
def main():
    win, msg, d1, d2, d3 = drawGUI()
    secretDoor(d1, d2, d3)
    getInput(win, d1, d2, d3)
    result(msg, d1, d2, d3)
    exit(win)


def drawGUI():
    win = GraphWin('Three Button Game', 390, 300)
    win.setCoords(0, 0, 130, 100)
    win.setBackground('white')

    d1 = Button(win, Point(25, 60), 30, 53, 'Door 1')
    d2 = Button(win, Point(65, 60), 30, 53, 'Door 2')
    d3 = Button(win, Point(105, 60), 30, 53, 'Door 3')

    title = Text(Point(65, 95), 'Three Button Game')
    title.setSize(17)
    title.draw(win)

    msgBox = Rectangle(Point(10, 25), Point(120, 9))
    msgBox.setFill('gray')
    msgBox.setWidth(0)
    msgBox.draw(win)

    msg = Text(Point(65, 17), 'Guess which one is a correct exit door?')
    msg.setSize(13)
    msg.draw(win)

    return win, msg, d1, d2, d3


def secretDoor(d1, d2, d3):
    i = randrange(1, 4)

    if i == 1:
        d1.setSecret()
    elif i == 2:
        d2.setSecret()
    else:
        d3.setSecret()


def getInput(win, d1, d2, d3):
    p = win.getMouse()

    while not d1.clicked(p) and not d2.clicked(p) and not d3.clicked(p):
        p = win.getMouse()


def result(msg, d1, d2, d3):

    x = d1.reveal()
    y = d2.reveal()
    z = d3.reveal()

    if x == 'win' or y == 'win' or z == 'win':
        msg.setText('You win!\nClick anywhere to close!')

    else:
        if x == 'secret':
            wayout = '1'
        elif y == 'secret':
            wayout = '2'
        else:
            wayout = '3'

        msg.setText('You lose! the correct door is door {}!\
        \nClick anywhere to close!'.format(wayout))


def exit(win):
    win.getMouse()
    win.close()


if __name__ == '__main__': main()