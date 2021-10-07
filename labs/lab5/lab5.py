"""
Name: Boomer Jenks
Lab5.py
"""

from graphics import *



def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)
    r = win_width / 10
    circle = Circle(Point(250, 250), 5 * r)
    circle.setFill("white")
    circle.draw(win)
    circle = Circle(Point(250, 250), 4 * r)
    circle.setFill("black")
    circle.draw(win)
    circle = Circle(Point(250, 250), r)
    circle.setFill("red")
    circle.draw(win)
    circle = Circle(Point(250, 250), r)
    circle.setFill("yellow")
    circle.draw(win)
    # area code here to get the dimentions and draw the target

    # wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("draw a triangle", win_width, win_height)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    t = Polygon(p1, p2, p3)
    side1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    side2 = math.sqrt((p3.getX() - p2.getX()) ** 2 + (p3.getY() - p2.getY()) ** 2)
    side3 = math.sqrt((p3.getX() - p1.getX()) ** 2 + (p3.getY() - p1.getY()) ** 2)
    perimeter = side1 + side2 + side3
    s = (side1 + side2 + side3)/2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    t.setOutline("blue")
    t.setFill("blue")
    t.draw(win)
    inst_pt = Point(200, 350)
    inst_pt2 = Point(200, 400)
    instructions = Text(inst_pt, "the area is: " + str(area))
    instructions2 = Text(inst_pt2, "the perimeter is: " + str(perimeter))
    instructions.draw(win)
    instructions2.draw(win)

    win.getMouse()
    win.close()


def color_shape():
    win_width = 400
    win_height = 400
    win = GraphWin("color shape", win_width, win_height)
    win.setBackground("white")

    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "green: ")
    green_text.setTextColor("green")

    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "blue: ")
    blue_text.setTextColor("blue")

    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_box = Entry(Point(win_width / 2+2, win_height / 2 + 40), 5)
    green_box = Entry(Point(win_width / 2+2, win_height / 2 + 70), 5)
    blue_box = Entry(Point(win_width / 2+2, win_height / 2 + 100), 5)

    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    for i in range(5):
        win.getMouse()
        red = int(red_box.getText())
        blue = int(blue_box.getText())
        green = int(green_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)

    win.getMouse()
    win.close()


def process_string():
    s = input("enter a string")
    print(s[0])
    print(s[-1])
    print(s[2:6])
    print(s[0] + s[-1])
    print(s[0] + s[-1])
    print(s[0:3] * 10)
    for i in range(len(s)):
        c = s[i]
        print(c)
    print(len(s))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    x = eval(input("enter the terms in the series: "))
    acc = 0
    for i in range(x):
        y = 2 + 2 * (i % 3)
        acc = acc + y
        print(y, end=" ")
    print("sum", acc)


def main():
    target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()

main()
