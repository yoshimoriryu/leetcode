from typing import List

# beats => rt: 39.31%; mem: 61.84%
class Solution:
    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # r w b 0 1 2
        n = len(nums)
        flag = False
        while not flag:
            flag = True
            i = 0
            while i < n:
                if i+1 < n:
                    if nums[i] > nums[i+1]:
                        temp = nums[i]
                        nums[i] = nums[i+1]
                        nums[i+1] = temp
                        flag = False
                i += 1
        print(nums)

# dutch partitioning problem; solution
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            
                