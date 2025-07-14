class Solution:
    def twoSum(self, nums, target: int):
        array = nums.copy()
        sum_array = []

        for idx, n in enumerate(array):
            index = array.index(n - target)

            if index >= 0:
                return idx, index

Solution().twoSum([1, 5, 0], 6)