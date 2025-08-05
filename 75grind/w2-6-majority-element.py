from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_d = {}
        max_key = -1
        max_val = -1
        for i in range(len(nums)):
            if nums[i] in nums_d:
                nums_d[nums[i]] += 1
                if nums_d[nums[i]] > max_val:
                    max_val = nums_d[nums[i]]
                    max_key = nums[i]
            else:
                nums_d[nums[i]] = 1
        if max_key == -1:
            return nums[0]
        return max_key

    #booyer-moore majority voting
    def majorityElement1(self, nums: List[int]) -> int:
        candidate = -1
        votes = 0
        for i in range(len(nums)):
            if votes == 0:
                candidate = nums[i]
                votes = 1
            else:
                if candidate == nums[i]:
                    votes += 1
                else:
                    votes -= 1
        
        return candidate

    def printAnswer(self, answer):
        print(answer)

if __name__ == "__main__":
    nums = [3,2,3]
    x = Solution()
    x.printAnswer(x.majorityElement(nums))
