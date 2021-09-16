"""
Name: Boomer Jenks
<Lab3>.py
"""
def average():
    hw = eval(input("enter the total amount of assignments: "))
    acc = 0
    for i in range(hw):
        total = eval(input("enter your grade on the Homework: " + str(i+1) + ": "))
        acc = acc + total
    average = acc / hw
    print("total hw average: ", average)
average()

def tip_jar():
    acc = 0
    for i in range(5):
        amount = eval(input("how much $ are you donating?: "))
        acc = acc + amount
        print(acc)
tip_jar()

def newton():
    x = eval(input("what is the number you are trying to find the root of?: "))
    refine = eval(input("how many times do you want to refine this number?: "))
    aprox = x / 2
    for i in range(refine):
        aprox = ((aprox + (x / aprox ))/2)
    print(x, aprox)
newton()

def sequence():
    x = eval(input("how many terms are in the sequence?: "))
    for i in range(1, x + 1):
        y = 1 + (i // 2 * 2)
        print(y, end= " ")
    print()
sequence()


def pi():
    terms = eval(input("enter the amount of terms in your given series: "))
    acc = 1
    for i in range(terms):
        num = 2 + (i//2*2)
        den = 1 + ((i+1)//2*2)
        acc = acc * (num / den)
    print(acc * 2)
pi()

