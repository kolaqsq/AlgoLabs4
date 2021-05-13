import errno
import os
import sys
import time

# reading array from file
file = open(sys.argv[1], "r")
# file = open('arr_unique_10.txt', "r")
length = int(file.readline())
file.readline()
arr = [int(x) for x in file.readline().split(" ")]
file.close()

# start time
start = time.time()

# sorting algorithm
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

# stop time
finish = time.time()
# print(arr)

# creating result file
filename = "./results/insertion_{}".format(sys.argv[1])
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

# saving result
result = open(filename, "w+")
result.write("{}\n\n{}\n\n".format(len(arr), finish - start))

for i in range(len(arr)):
    result.write("{} ".format(arr[i]))
result.close()
