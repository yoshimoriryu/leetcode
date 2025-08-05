from typing import List

# TLE at tc 75/87
class SolutionX:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        minimums = []
        len_arr = 1
        while len_arr <= n:
            i = 0
            while len_arr+i < n+1:
                sub_arr = arr[i:len_arr+i]
                i += 1
                minimums.append(min(sub_arr))
            len_arr += 1

        return sum(minimums)%(10**9 + 7)

# failed to solve
class Solution:
  def sumSubarrayMins(self, A: List[int]) -> int:
        A = [0] + A + [0]
        stack = []
        res = 0
        for i in range(len(A)):
            print(i, res, stack)
            while stack and A[i] < A[stack[-1]]:
                cur = stack.pop()
                left = stack[-1] 
                right = i
                print('#', cur, left, right)
                res += A[cur]*(right-cur)*(cur-left)
            stack.append(i)
        return res%(10**9+7)

x = Solution()
arr = [3,1,2,4]
print(x.sumSubarrayMins(arr))