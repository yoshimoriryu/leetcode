from typing import List

class Solution:
    # complexity: O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dup_nums = nums
        idx = 0
        found = False
        while dup_nums:
            # print('=-=')
            curr = dup_nums[0]
            dup_nums = dup_nums[1:]
            idx2 = idx + 1
            for i in range(len(dup_nums)):
                # print(curr, dup_nums[i])
                if curr + dup_nums[i] == target:
                    found = True
                    ans1 = curr
                    ans2 = dup_nums[i]
                    break
                idx2 = idx2 + 1
            if found:
                break
            else:
                idx = idx + 1
        return [idx, idx2]


    # complexity: O(n^2), good writing
    def twoSumGood(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []


    # complexity: O(n)
    def twoSumVeryGood(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_map = {}

        for i in range(n):
            complement = target - nums[i]
            print(i, nums[i], complement)
            if complement in nums_map:
                return [i, nums_map[complement]]
            nums_map[nums[i]] = i
            print(nums_map)
        return []
    
    def printAnswer(self, answer):
        print(answer)

if __name__ == "__main__":
    nums = [2,11,7,15]
    target = 9
    x = Solution()
    # x.printAnswer(x.twoSum(nums, target))
    # x.printAnswer(x.twoSumGood(nums, target))
    x.printAnswer(x.twoSumVeryGood(nums, target))
    

