import random
import sys


def default():
    file = open("arr_{}.txt".format(size), "w+")
    file.write("{}\n\n".format(size))
    first = True

    for i in range(int(size)):
        if first:
            file.write("{}".format(random.randint(0, int(size))))
            first = False
        else:
            file.write(" {}".format(random.randint(0, int(size))))

    file.close()


def unique():
    file = open("arr_unique_{}.txt".format(size), "w+")
    file.write("{}\n\n".format(size))
    temp = []
    first = True

    for i in range(int(size)):
        temp.append(i + 1)
    random.shuffle(temp)

    for j in range(len(temp)):
        if first:
            file.write("{}".format(temp[j]))
            first = False
        else:
            file.write(" {}".format(temp[j]))

    file.close()


def decr():
    file = open("arr_decr_{}.txt".format(size), "w+")
    file.write("{}\n\n".format(size))
    first = True

    for i in range(int(size), 0, -1):
        if first:
            file.write("{}".format(i))
            first = False
        else:
            file.write(" {}".format(i))

    file.close()


size = sys.argv[1]
if len(sys.argv) > 2:
    mode = sys.argv[2]
else:
    mode = "default"

if mode == "default":
    default()
elif mode == "unique":
    unique()
elif mode == "decr":
    decr()
