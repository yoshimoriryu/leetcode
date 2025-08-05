from typing import List
from copy import deepcopy

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        g_cp = deepcopy(grid)
        n = len(grid)

        g_rot = []
        i = 0
        while i < n:
            j = 0
            y = []
            while j < n:
                y.append(grid[j][i])
                j += 1
            g_rot.append(y)
            i += 1

        i,count = 0,0
        while i < n:
            j = 0
            print(i,j)
            while j < n:
                g_cp[i][j] = min(max(grid[i]), max(g_rot[j]))
                if g_cp[i][j] != grid[i][j]:
                    count += (g_cp[i][j] - grid[i][j])
                j +=1
            i += 1
        return g_cp
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
x = Solution()
print(x.maxIncreaseKeepingSkyline(grid))