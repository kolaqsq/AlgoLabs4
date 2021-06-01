class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        nth_bit = 1 << n

        for i in range(2 ** n):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i | nth_bit)[3:]

        # crazy hamburger
        # for i in range(2 ** n, 2 ** (n + 1)):
        #     # generate bitmask, from 0..00 to 1..11
        #     bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output
