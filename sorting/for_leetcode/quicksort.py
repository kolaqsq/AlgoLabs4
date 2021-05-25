class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(arr, begin, end):
            if end - begin <= 1:
                return

            pivot = partition(arr, begin, end)
            quicksort(arr, begin, pivot), quicksort(arr, pivot + 1, end)

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

        quicksort(nums, 0, len(nums))
        return nums
