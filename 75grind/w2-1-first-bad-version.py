# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low_n = 1
        t_flag = -1
        f_flag = -1
        while low_n <= n:
            if t_flag > f_flag and t_flag-f_flag == 1:
                return t_flag
            mid = (n + low_n) // 2
            if isBadVersion(mid):
                n = mid - 1
                t_flag = mid
            else:
                low_n = mid + 1
                f_flag = mid
        return t_flag
    
    def firstBadVersion1(self, n):
        i = 1
        j = n
        while (i < j):
            pivot = (i+j) // 2
            if (isBadVersion(pivot)):
                j = pivot       # keep track of the leftmost bad version
            else:
                i = pivot + 1   # the one after the rightmost good version
        return i