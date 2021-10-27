# create a list of associated letter grades from 0-10
def weighted_average():
    class_avg = 0
    line_acc = 0
    infile = open("grades.txt", "r")
    out_file_name = open("avg.txt", 'w')  # open the output file for writing

# open the input file
    with open("grades.txt") as fp:
        contents = fp.readlines()  # read the contents of the file into the list with each line being an element of the list

    # loop over the contents list
        for line in contents:
            line_acc += 1
            split1 = line.split(":")
            var = split1[1]
            split2 = var.split()
            acc = 0
            for i in range(0, len(split2), 2):
                acc += eval(split2[i])
            if acc > 100:
                out_file_name.write(split1[0] + "error the weight is over 100" + "\n")
            elif acc < 100:
                out_file_name.write(split1[0] + "error the weight is under 100" + "\n")
            else:
                acc1 = 0
                for j in range(0 ,len(split2), 2):
                    acc1 += eval(split2[j]) * eval(split2[j+1])
                acc1 = acc1 / 100
                class_avg += acc1
                out_file_name.write(split1[0])
                out_file_name.write(str(acc1)+"\n")
        class_avg = class_avg/line_acc
        out_file_name.write("this the class average: " + str(class_avg))
weighted_average()