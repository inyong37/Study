from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        return sum
