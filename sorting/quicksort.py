import errno
import os
import sys
import time

# sorting algorithm
def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array


# def quicksort2(array):
#     less = []
#     greater = []
#
#     if len(array) > 1:
#         pivot = array[0]
#         for i in range(1, len(array)):
#             if array[i] < pivot:
#                 less.append(array[i])
#             else:
#                 greater.append(array[i])
#         return quicksort(less) + [pivot] + quicksort(greater)
#     else:
#         return array


# reading array from file
file = open(sys.argv[1], "r")
# file = open('arr_unique_10.txt', "r")
length = int(file.readline())
file.readline()
arr = [int(x) for x in file.readline().split(" ")]
file.close()

# start time
start = time.time()

# start algorithm
arr = quicksort(arr)
# arr = quicksort2([5, 2, 3, 1])

# stop time
finish = time.time()
print(arr)

# creating result file
filename = "./results/quicksort_{}".format(sys.argv[1])
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
