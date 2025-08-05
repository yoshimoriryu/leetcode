from typing import List
import heapq

class Solution:
    # failed to solve; revisit count: 1; success: 1
    def kClosest1(self, points: List[List[int]], k: int) -> List[List[int]]:
        highest_score = 9999999
        ans = []
        for i in range(len(points)):
            curr_score = self.sqrtScore(points[i])
            if curr_score < highest_score:
                ans.insert(0, points[i])
            else:
                ans.append(points[i])
            highest_score = curr_score
        return ans[:k]

    # the key is heappushpop, pushing the smallest value out
    # thats why dist using negative value, to get rid the farthest point
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x,y) in points:
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
            print(x,y,dist)
        return [(x,y) for (dist,x,y) in heap]

    def sqrtScore(self, point):
        return point[0]*point[0] + point[1]*point[1]

    def printAnswer(self, answer):
        print(answer)

# LMAO THIS IS NOT MINE, SOLUTION
class SolutionKey:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0] * x[0] + x[1] * x[1])[:k]

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(points, k)
x = Solution()
x.printAnswer(x.kClosest(points, k))