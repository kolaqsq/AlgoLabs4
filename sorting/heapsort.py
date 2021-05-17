import errno
import os
import sys
import time


# sorting algorithm
def heapify(array, n, m):
    largest = m
    left = 2 * m + 1
    right = 2 * m + 2

    if left < n and array[largest] < array[left]:
        largest = left

    if right < n and array[largest] < array[right]:
        largest = right

    if largest != m:
        array[m], array[largest] = array[largest], array[m]

        heapify(array, n, largest)


def heapsort(array):
    n = len(array)

    for k in range(n // 2 - 1, -1, -1):
        heapify(array, n, k)

    for k in range(n - 1, 0, -1):
        array[k], array[0] = array[0], array[k]
        heapify(array, k, 0)

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

# start algorithm
arr = heapsort(arr)

# stop time
finish = time.time()
# print(arr)

# creating result file
filename = "./results/heapsort_{}".format(sys.argv[1])
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
