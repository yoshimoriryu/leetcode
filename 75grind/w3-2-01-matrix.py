from typing import List
from collections import deque

# failed to solve; revisit count: 1
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        MAX_VALUE = m*n

        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([i,j])
                if mat[i][j] == 1:
                    mat[i][j] = MAX_VALUE

        direct = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            x,y = queue.popleft()
            for r,c in direct:
                if 0 <= x+r < m and 0 <= y+c < n and mat[x][y] + 1 < mat[x+r][y+c]:
                    mat[x+r][y+c] = mat[x][y] + 1
                    queue.append([x+r,y+c])
        return mat

class SolutionKey:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        queue = deque()
        MAX_VALUE = m * n
        
        # Initialize the queue with all 0s and set cells with 1s to MAX_VALUE.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = MAX_VALUE
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and mat[r][c] > mat[row][col] + 1:
                    print(mat[r][c], mat[row][col] + 1)
                    queue.append((r, c))
                    mat[r][c] = mat[row][col] + 1
        return mat

    def printAnswer(self, answer):
        print(answer)

mat = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]]
print(mat)
x = SolutionKey()
x.printAnswer(x.updateMatrix(mat))


