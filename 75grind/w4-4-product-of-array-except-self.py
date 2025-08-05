class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 1
        zeros = [-1 for i in range(len(nums))]
        for i in range(len(nums)):
            print('ini x',x)
            if nums[i] == 0:
                zeros[i] = 0
            x  = x*nums[i] if nums[i] != 0 else x

        zeros_count = 0
        for i in zeros:
            if i == 0:
                zeros_count += 1
        print(zeros_count, x)

        ans = []
        for i in nums:
            if not zeros_count:
                ans.append(x//i)
            elif zeros_count == 1:
                if i == 0:
                    ans.append(x)
                else:
                    ans.append(0)
            else:
                ans.append(0)
        return ans