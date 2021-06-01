class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ i >> 1 for i in range(2 ** n)]


# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         result = []
#         for i in range(2 ** n):
#             result.append(i ^ i >> 1)
#         return result
