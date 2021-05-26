def create_array(p, n, q, v):
    arr = [p]
    for i in range(1, n):
        arr.append((arr[i - 1] * q) % v)

    return arr


def k_th(arr, begin, end, k):
    if end - begin <= 1:
        return
    pivot = partition(arr, begin, end)

    if pivot == k:
        return
    elif k < pivot:
        k_th(arr, begin, pivot, k)
    else:
        k_th(arr, pivot + 1, end, k)


def new_k_th(arr, k):
    begin, end = 0, len(arr)
    while True:
        if end - begin <= 1:
            return

        pivot = partition(arr, begin, end)

        if pivot == k:
            return
        elif k < pivot:
            end = pivot
        else:
            begin = pivot + 1


def partition(arr, begin, end):
    arr[end - 1], arr[(begin + end - 1) // 2], pindex = \
        arr[(begin + end - 1) // 2], arr[end - 1], begin

    for j in range(begin, end):
        if arr[j] < arr[end - 1]:
            arr[pindex], arr[j], pindex = \
                arr[j], arr[pindex], pindex + 1

    arr[end - 1], arr[pindex] = \
        arr[pindex], arr[end - 1]
    return pindex


# Q, V, P, N, K = 343, 32767, 3, 10, 7
Q, V, P, N, K = [int(x) for x in input().split()]
array = create_array(P, N, Q, V)
# k_th(array, 0, len(array), K)
new_k_th(array, K)

print(array[K - 1])
