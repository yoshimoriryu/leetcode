from typing import List

class Solution:
    # TLE bang
    # def prod(self, nums: List[int]):
    #     res = 1
    #     for el in nums:
    #         res *= el
    #     return res

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     ans = []
    #     n = len(nums)
    #     for i in range(len(nums)):
    #         ans.append(self.prod(nums[0:i]) * self.prod(nums[i+1:n]))
    #     return ans

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1]
        suff = [1]
        rev_nums = nums[::-1]
        print('nums: ', nums, rev_nums)

        prod = 1
        for i, el in enumerate(nums):
            prod *= el
            pref.append(prod)
        pref = pref[:len(pref)-1]
        print("this is pref", pref)

        prod = 1
        for i, el in enumerate(rev_nums):
            prod *= el
            suff.append(prod)
        suff = suff[:len(suff)-1]
        suff = suff[::-1]
        print("this is suff", suff)

        ans = []
        for i,j in zip(pref, suff):
            ans.append(i*j)
        return ans


nums = [1,2,3,4]
x = Solution()
print(x.productExceptSelf(nums))

