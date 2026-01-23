from typing import List
import bisect

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        if nums_sorted == nums:
            return 0
        
        MAX_INT = 10**20
        # how to count or find the minimum sum in nums?


        nums_set = set(nums)
        nums_sorted = sorted(nums)
        ct = 0
        while nums_sorted != nums:
            min_sum = MAX_INT
            sums = []
            i = 0
            n = len(nums)
            min_idx = -1
            while i < n-1:
                x = nums[i] + nums[i+1]
                sums.append(x)
                old_min = min_sum
                min_sum = min(min_sum, x)
                if min_sum != old_min:
                    min_idx = i
                else:
                    min_idx = min_idx
                i += 1
            # use bisect.bisect_left to search for index of minimum
            import bisect
            print(f"sums, min_sum, leftmost_idx {sums} {min_sum} {min_idx}")
            new_nums = nums[:min_idx] + [sums[min_idx]] + nums[min_idx+2:n]

            print(f"new_nums: {new_nums}")
            nums = new_nums
            nums_sorted = sorted(nums)
            ct += 1
        return ct
    

nums = [5,2,3,1]
# nums = [2,2,-1,3,-2,2,1,1,1,0,-1]
print(nums)

x = Solution()
y = x.minimumPairRemoval(nums)
print(f"ans {y}")