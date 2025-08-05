class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n_len = len(nums)
        new_len = len(set(nums))
        return not n_len == new_len