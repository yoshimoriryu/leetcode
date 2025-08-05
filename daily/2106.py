'''
hard, credit: https://www.youtube.com/watch?v=lSvUS-0jeWw&t=8s&ab_channel=ProgrammingLivewithLarry
'''
from typing import List
import bisect

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        f1 = []
        start_fruit = 0
        for x,t in fruits:
            if startPos == x:
                start_fruit = t
                continue
            f1.append([x,t])
        def calc(fruits):
            INF = 10 ** 20
            N = len(fruits)

            prefix = [(-INF,0)]
            for x, t in fruits:
                prefix.append((x, t + prefix[-1][1]))
            # print(fruits, "//", prefix, startPos)

            fruits_left = 0
            # how many fruits on the left side from startPos
            pindex = bisect.bisect_left(prefix, (startPos, -1))
            fruits_left = prefix[pindex-1][1]

            # let's start by going to the right
            current = bisect.bisect_left(fruits, [startPos, -1])

            best = 0
            f = 0
            for right in range(current, N):
                # go to the right to the index "right"
                dist = fruits[right][0] - startPos
                if dist > k:
                    continue

                f += fruits[right][1]

                # f fruits going to the right
                remaining = k - dist * 2

                left_pos = startPos - remaining # after snatching all right side, this is the reach we can go to left [relative to startPos]

                if left_pos < startPos:
                    # fruits between left_pos and startPos
                    lindex = bisect.bisect_right(prefix, (left_pos, -1))
                    fruits_left_now = fruits_left - prefix[lindex - 1][1]
                else:
                    fruits_left_now = 0

                best = max(best, fruits_left_now + f)

            # print("best: ", best)
            return best
        right_to_left = calc(f1)
        f2  = []
        for x,t in f1:
            f2.append([-x, t])
        f2.sort()
        startPos = -startPos
        left_to_right = calc(f2)

        return max(right_to_left, left_to_right) + start_fruit

fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
# fruits = [[2,8],[6,3],[8,6]]
startPos = 5
k = 4
x = Solution()
print(x.maxTotalFruits(fruits,startPos,k))