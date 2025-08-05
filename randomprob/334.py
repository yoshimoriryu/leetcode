from typing import List
import math

class Solution:
    # TLE bang
    # def increasingTriplet(self, nums: List[int]) -> bool:
        # left,mid,right = 0,1,2
        # n = len(nums)
        # if n < 3:
        #     return False

        # while nums[left] >= nums[mid] or nums[mid] >= nums[right]:
        #     print(left, mid, right, ";", nums[left], nums[mid], nums[right])
        #     while mid < n and nums[mid] <= nums[left]:
        #         mid += 1
        #     if mid == n:
        #         left, mid, right = left+1, left+2, left+3
        #         if left >= n-2:
        #             return False

        #     else:
        #         right = mid+1
        #         while right < n and nums[right] <= nums[mid]:
        #             right += 1
        #         if right == n:
        #             mid, right = mid+1, mid+2
                    
        #             if mid >= n-1:
        #                 left, mid, right = left+1, left+2, left+3
        #                 if left >= n-2:
        #                     return False
                
        # print("out", left, mid, right, ";", nums[left], nums[mid], nums[right])
        # return True if left < mid < right and nums[left] < nums[mid] < nums[right] else False

    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     print(nums)
    #     n = len(nums)
    #     maxRight = [0] * n  # maxRight[i] is the maximum element among nums[i+1...n-1]
    #     maxRight[-1] = nums[-1]
    #     print(maxRight)
    #     for i in range(n-2, -1, -1):
    #         maxRight[i] = max(maxRight[i+1], nums[i+1])
    #     print(maxRight)
            
    #     minLeft = nums[0]
    #     for i in range(1, n-1):
    #         print(minLeft)
    #         if minLeft < nums[i] < maxRight[i]:
    #             return True
    #         minLeft = min(minLeft, nums[i])
    #     return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = math.inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:  # Now first < num, if num <= second then try to make `second` as small as possible
                second = num
            else:  # Now first < second < num
                return True
        return False

# x = [20,100,10,12,5,13]
x = [1,5,0,4,1,3]
y = Solution()
print(y.increasingTriplet(x))
