"""
Name: Boomer Jenks
lab12.py
"""
from random import randint
def find_and_remove(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Boomer Jenks"
    except:
        pass

def read_data(filename):
    f = open(filename, "r")
    d = f.readline()
    d = d.split()
    i = 0
    while i < len(d):
        d[i] = int(d[i])
        i += 1
    return d


def is_in_linear(value, lst):
    i = 0
    while i < len(lst):
        if value == lst[i]:
            return True
        i += 1
    return False


def good_input():
    x = eval(input("Enter a num in the range 1 - 10: "))
    while x not in range(1, 10):
        x = eval(input("enter a number within the range: "))
    return x


def num_digits():
    x = eval(input("input a positive int: "))
    while x > 0:
        i = 0
        while x != 0:
            i += 1
            x //= 10
        print("the number of digites is: ", i)
        x = eval(input("input a positive int: "))



def high_low():
    number = randint(1, 100)
    x = eval(input("enter a number between 1 and 100: "))
    guesses = 0
    while x != number and guesses < 7:
        if x < number:
            print("number is too low!")
        elif x > number:
            print("number is too high!")
        guesses += 1
        if x != number and guesses < 7:
            x = eval(input("enter another number between 1 and 100 "))
    if x == number:
        print("You Win!")
    else:
        print("You Lose:(")



def main():
    find_and_remove([1, 3, 4, 6, 9, 10], 3)

    good_input()
    num_digits()
    high_low()
main()
