class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(arr, heap_length, root):
            # Find largest among root and children
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2

            if left < heap_length and arr[left] > arr[largest]:
                largest = left

            if right < heap_length and arr[right] > arr[largest]:
                largest = right

            # If root is not largest, swap with largest and continue heapifying
            if largest != root:
                arr[root], arr[largest] = arr[largest], arr[root]

                heapify(arr, heap_length, largest)

        def heapsort(array):
            arr_length = len(array)

            # Build max heap
            for i in range(arr_length // 2, -1, -1):
                heapify(array, arr_length, i)

            for i in range(arr_length - 1, 0, -1):
                # Swap sorted with new root
                array[0], array[i] = array[i], array[0]

                # Heapify root
                heapify(array, i, 0)

        heapsort(nums)

        return nums
