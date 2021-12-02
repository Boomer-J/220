"""
Name: <Boomer Jenks>
lab13.py
"""

def iib(val, values):
    mid = values[len(values)//2]
    while mid != val and len(values)!=1:
        if mid > val:
            values = values[:len(values)//2]
        else:
            values = values[len(values)//2+1:]
        mid = len(values)//2
    if mid == val:
        return True
    else:
        return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = 1
        for j in range(i, len(values)):
            if j < lowest:
                lowest = values[j]
                pos = j
        values[i],values[pos] = values[pos], values[i]


def rectangles(values):
    d = {}
    areas = []
    for rect in values:
        d[get_area(rect)]=rect
        areas.append(get_area(rect))
    selection_sort(areas)
    for i in areas:
        values[i] = d[areas[i]]


def get_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    w = abs(p1.getX()-p2.getX())
    h = abs(p1.getY()-p2.getY())
    return w * h





def trade_alert(filename):
    infile = open(filename,"r")
    data = infile.read().split()
    second = 0
    for i in data:
        second = second + 1
        pos = int(i)
        if pos > 830:
            print(second, "Alert!!!")
        elif pos > 500:
            print(second, "Warning!")










def main():
    print(iib(3, [1, 2, 3, 4, 5]))
    trade_alert('trades.txt')
    pass

main()