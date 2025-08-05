from typing import List

class Solution:
    # BINARY SEARCH DEFINITION
    # REMEMBER: SORTED ONLY
    """
    Binary search is a searching algorithm that is used to find the 
    position of a target value in a sorted list of items. The 
    algorithm works by repeatedly dividing the search interval in 
    half and deciding which half of the search interval the target 
    value is in. The algorithm starts by comparing the target value 
    with the middle element of the list. If the target value is 
    equal to the middle element, the algorithm terminates and returns 
    the index of the middle element. 
    If the target value is less than the middle element, 
    the algorithm searches the left half of the list. 
    If the target value is greater than the middle element, 
    the algorithm searches the right half of the list. 
    The algorithm continues to divide the search interval in half 
    and search the appropriate half of the list until the target 
    value is found or the search interval is empty. 
    The time complexity of binary search is O(log n), 
    where n is the length of the input list. 
    The space complexity of binary search is O(1), 
    which means that the amount of memory used by the algorithm 
    does not depend on the size of the input 1.
    """
    
    # wrong, not a binary search dawg, this is considered linear search
    # why? because even though has low iteration, but the algorithm
    # itself must check each list element once
    def search1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        found = False
        idx = -1
        while i < n and not found:
            if nums[i] == target:
                idx = i
                break
            if i+1 < n:
                if nums[i+1] == target:
                    idx = i+1
                    break
            else:
                break
            i += 2
        return idx
            
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid, nums[mid])
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        return -1

    def printAnswer(self, answer):
        print(answer)

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    x = Solution()
    x.printAnswer(x.search(nums, target))