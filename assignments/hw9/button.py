from graphics import *
class Button:

    def __init__(self, win, center, width, height, label):

        self.secret = 0

        self.hasClick = 0

        x, y = center.getX(), center.getY()
        self.xmin, self.xmax = x - width / 2, x + width / 2
        self.ymin, self.ymax = y - height / 2, y + height / 2

        self.rec = Rectangle(Point(self.xmin, self.ymax), Point(self.xmax, self.ymin))
        self.rec.setFill(color_rgb(255, 247, 133))
        self.rec.setWidth(0)
        self.rec.draw(win)

        self.knob2 = Circle(Point(x + (width / 3), y - (height / 100)), width / 12)
        self.knob2.setFill(color_rgb(231, 205, 20))
        self.knob2.setWidth(0)
        self.knob2.draw(win)

        self.knob1 = Circle(Point(x + (width / 3.15), y), width / 12)
        self.knob1.setFill(color_rgb(255, 229, 40))
        self.knob1.setWidth(0)
        self.knob1.draw(win)

        self.label2 = Rectangle(Point(x - (width / 3), y + (height / 2.5)), Point(x + (width / 3), y + +(height / 3.8)))
        self.label2.setFill(color_rgb(231, 205, 20))
        self.label2.setWidth(0)
        self.label2.draw(win)

        self.label1 = Rectangle(Point(x - (width / 2.8), y + (height / 2.35)),
                                Point(x + (width / 3.2), y + +(height / 3.6)))
        self.label1.setFill(color_rgb(255, 229, 40))
        self.label1.setWidth(0)
        self.label1.draw(win)

        self.text = Text(Point(x, y + (height / 2.8)), label)
        self.text.setSize(10)
        self.text.draw(win)

    def setSecret(self):
        '''Set this door to a secret door.'''
        self.secret = 1
        print()

    def turnGreen(self):
        '''Turn door color to green to present this is a correct door.'''
        self.rec.setFill(color_rgb(51, 229, 70))
        self.knob2.setFill(color_rgb(51, 176, 0))
        self.knob1.setFill(color_rgb(62, 200, 0))
        self.label2.setFill(color_rgb(51, 176, 0))
        self.label1.setFill(color_rgb(62, 200, 0))

    def turnRed(self):
        '''Turn door to red if user click on wrong door.'''
        self.rec.setFill(color_rgb(234, 53, 65))
        self.knob2.setFill(color_rgb(142, 33, 41))
        self.knob1.setFill(color_rgb(240, 49, 61))
        self.label2.setFill(color_rgb(142, 33, 41))
        self.label1.setFill(color_rgb(240, 49, 61))

    def clicked(self, p):
        '''Remember if door has click by user
        and also return Bool data'''
        if self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax:
            self.hasClick = 1

        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def reveal(self):
        '''Key door feature. It will check self.secret and self.hasClcik
        and respond accordingly to both action.'''

        if self.secret == 1 and self.hasClick == 1:

            self.turnGreen()
            return 'win'


        elif self.secret == 0 and self.hasClick == 1:
            self.turnRed()


        elif self.secret == 1 and self.hasClick == 0:
            self.turnGreen()
            return 'secret'
