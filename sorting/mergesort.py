import errno
import os
import sys
import time


# sorting algorithm
def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergesort(left)
        mergesort(right)

        n = 0
        m = 0
        k = 0

        # merge
        while n < len(left) and m < len(right):
            if left[n] < right[m]:
                array[k] = left[n]
                n += 1
            else:
                array[k] = right[m]
                m += 1
            k += 1

        # adding merge leftovers
        while n < len(left):
            array[k] = left[n]
            n += 1
            k += 1

        while m < len(right):
            array[k] = right[m]
            m += 1
            k += 1
    return array


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
arr = mergesort(arr)

# stop time
finish = time.time()
# print(arr)

# creating result file
filename = "./results/mergesort_{}".format(sys.argv[1])
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
