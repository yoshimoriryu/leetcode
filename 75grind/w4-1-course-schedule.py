from typing import List
from collections import deque

# failed to solve; revisit count: 1
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        ans = []

        # create adjacent list
        for course, p in prerequisites:
            adj[p].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            ans.append(curr)

            for course in adj[curr]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        return len(ans) == n

    def buildAdjacencyList(self, n, edgesList):
            adjList = [[] for _ in range(n)]
            # c2 (course 2) is a prerequisite of c1 (course 1)
            # i.e c2c1 is a directed edge in the graph
            for c1, c2 in edgesList:
                adjList[c2].append(c1)
            return adjList

x = Solution()
numCourses = 3
prerequisites = [[1,0], [1,3], [1,4]]
print(x.canFinish(numCourses, prerequisites))

n = len(prerequisites)
print(x.buildAdjacencyList(n,prerequisites))