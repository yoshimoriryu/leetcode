from typing import List

# failed to solve
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m,n = len(grid), len(grid[0])
        ans = 0
        
        def dfs(i,j):
            grid[i][j] = '2'
            for di,dj in (0,1), (0,-1), (1,0), (-1,0):
                ii, jj = i+di, j+dj
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == '1':
                    dfs(ii,jj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    print('sini1', grid)
                    dfs(i,j)
                    print('sini2', grid)
                    ans += 1
        return ans

                    
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
x = Solution()
print(x.numIslands(grid))