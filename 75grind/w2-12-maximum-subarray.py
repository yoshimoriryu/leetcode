import sys

NEGATIVEINT = -sys.maxsize

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            local_max = NEGATIVEINT
            global_max = NEGATIVEINT
            for i in range(len(nums)):
                local_max = max(nums[i], nums[i] + local_max)
                if local_max > global_max:
                    global_max = local_max
            return global_max
