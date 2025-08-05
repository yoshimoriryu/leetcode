from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        prefix = [(-1,0)]
        for x, t in fruits:
            prefix.append((x, t + prefix[-1][1]))
        print(fruits)
        print(prefix)
        return

fruits = [[2,8],[6,3],[8,6]]
startPos = 5
k = 4
x = Solution()
print(x.maxTotalFruits(fruits,startPos,k))