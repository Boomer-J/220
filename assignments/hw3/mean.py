"""
name: Jenks, Boomer
mean_test.py

Problem: write a Python program designed to output the RMS (root-mean-square),
the Harmonic Mean and the Geometric Mean.

Certification of authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def main():
#the program will take 5 upperbound inputs inorder to calculate the Root-mean-square average,
#the Harmonic mean as well as the geometric mean
#the inputs will be any given set of numbers where the output will calculate
#the sum of those numbers and divide by the amount of numbers used
    starting_num = eval(input("Input the number of intergers you would like to calculate: "))
    acc = 0
    acc1 = 0
    acc2 = 1
    for i in range(starting_num):
        total = eval(input("enter the the number set: " + str(i + 1) + ":"))
        acc = acc + (total ** 2)
        mean = acc / starting_num
        root_mean_square = math.sqrt(mean)
        acc1 = acc1 + 1 / total
        harmonic_mean = starting_num / acc1
        acc2 = acc2 * total
        geometric_mean = acc2 ** (1/starting_num)
    root_mean_square2 = round(root_mean_square, 3)
    harmonic_mean2 = round(harmonic_mean, 3)
    geometric_mean2 = round(geometric_mean, 3)
    print(root_mean_square2)
    print(harmonic_mean2)
    print(geometric_mean2)
