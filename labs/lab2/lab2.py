"""
Name: Boomer Jenks
lab2.py
"""
import math
def sum_of_threes():
    bound = eval(input("enter the upper bound:"))
    acc = 0
    for x in range(0, bound+1, 3):
        acc = acc+x
    print(acc)
sum_of_threes()
def muliplication_table():
    for h in range(1, 11):
        print()
        for l in range(1, 11):
            print(h * l, end=" ")
h = 1
l = 1
muliplication_table()

def triangle_area():
    a = eval(input("enter length of side a:"))
    b = eval(input("enter length of side b:"))
    c = eval(input("enter length of side c:"))
    s = (a + b + c) / 2
    a = math.sqrt(s * (s - a))
    a = math.sqrt(a)
    print(s)
triangle_area()

def sumSquares():
    start = eval(input("enter your starting number:"))
    ending = eval(input("enter your second number:"))
    for u in range (start, ending+1):
        acc1 = u ** 2
        acc2 = acc1 + u ** 2
        math.pow(u, 2)
        print(acc2)
sumSquares()
def power():
    base = eval(input("enter starting number:"))
    exp = eval(input("enter exp:"))
    acc = 1
    for x in range(exp):
        acc = acc * base
    print(acc)
power()