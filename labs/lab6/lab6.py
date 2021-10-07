"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def name_reverse():

    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    x = input("What's your first and last name?: ")
    split = x.split(" ")
    print(split[1] + ", " + split[0])


def comp_name():
    x = input("Enter the Internet domain name: ")
    split = x.split(".")
    print(split[1])

def names():
    x = input("enter peoples names using commas to separate names: ")
    n = x.split(", ")
    for name in n:
        ini = name.split(" ")
        print("The initials are: ", ini[0][0] + ini[1][0])

def initials():
    n = eval(input("Enter the number of students in the class: "))
    for i in range(n):
        first = input("Enter the first name of student: " + str(i+1) + ": ")
        last = input("Enter the last name of the student: " + str(i+1) + ": ")
        print(first + "'s initials are: ", first[0] + last[0])

def thirds():
    n = eval(input("How many sentences are being entered?: "))
    for i in range(n):
        x = input("what is sentence?: " + str(i + 1) + " ")
        print(x[2::3])

def word_average():
    x = input("enter a sentence: ")
    acc = 0
    words = x.split(" ")
    for word in words:
        acc = len(word) + acc
        print(acc / len(words))

def pig_latin():
    x = input("enter a sentance: ").lower()
    words = x.split(" ")
    for word in words:
        pig = (word[1:] + word[0] + "ay")
        print(pig, end=" ")


def main():
    #name_reverse()
    #comp_name()
    #names()
    #initials()
    thirds()
    #word_average()
    #pig_latin()


main()
