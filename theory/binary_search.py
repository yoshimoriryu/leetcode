# i want to exercise my binary search:
from typing import List
def binarySearch(arr: List, target: int):
  left = 0
  right = len(arr)-1
  while left <= right:
    mid = (left + right) //2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      right = mid - 1
    elif arr[mid] < target:
      left = mid + 1
  return -1


arr = [1, 3, 5, 7, 9, 11]
target = 11
print(binarySearch(arr,target))
