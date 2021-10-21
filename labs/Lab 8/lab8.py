"""
Name: <Boomer Jenks>
<lab8>.py
"""
from encryption import encode, encode_better
def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    output = open(out_file_name, "w+") #+
    i = 1
    for line in infile:
        words = line.split(" ")
        for word in words:
            output.write(str(i) + word + "\n")
            i += 1



def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    output = open(out_file_name, "w+")
    for line in infile:
        parts = line.split(" ")

        wage = float(parts[2])
        wage = 1.65 + wage                 #raise added to wage
        wage = wage * int(parts[3])
        output.write(parts[0] + " " + parts[1] + " " + str(wage)+"\n")

def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10-i
        acc += (pos * int(isbn[i]))
    return acc


def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(line)


def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(encode(line, key))


def send_uncrackable_message(file, friend, pad):
    #from encryption import
    infile = open(file, "r")
    output = open(friend, "w")
    padfile = open(pad, "r")
    key = padfile.read()
    for line in infile:
        output.write(encode_better(line, key)+ "\n")

def main():
    #number_words("Walrus.txt", "walrusoutput.txt")
    #hourly_wages("hourly_wages.txt", "output_hour_wages.txt")
    #print(calc_check_sum("0072946520"))
    #send_message("message.txt", "boomer")
    #send_safe_message("message.txt", "boomer" , 3)
    send_uncrackable_message("safest_message.txt", "boomer", "pad.txt")
    # add other function calls here
    pass


main()