import errno
import os
import sys
import time

file = open(sys.argv[1], "r")
length = int(file.readline())
file.readline()
arr = [int(x) for x in file.readline().split(" ")]

start = time.time()
for i in range(1, len(arr)):
    key = arr[i]

    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
finish = time.time()

filename = "./results/insertion_{}".format(sys.argv[1])
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

result = open(filename, "w+")
result.write("{}\n\n{}\n\n".format(len(arr), finish - start))

for i in range(len(arr)):
    result.write("{} ".format(arr[i]))
