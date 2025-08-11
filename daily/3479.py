from typing import List
import bisect

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        INF = 10 ** 20
        N = len(baskets)
        baskets_idx = sorted((basket, i) for i, basket in enumerate(baskets))
        print(baskets_idx)
        baskets.sort()
        print(baskets)

        def segmentTree(arr): # will proccess baskets_idx
            N = len(arr)
            tree = [(INF,INF)] * N * 2
            for i in range(N):
                tree[i + N] = arr[i]
            for i in range(N-1, 0, -1):
                tree[i] = min(tree[i * 2], tree[i * 2 + 1])
            print("seg tree", tree)
        
        def updateTree(N, tree, idx, val):
            idx += N
            tree[idx] = val
            while idx > 1:
                idx //= 2
                tree[idx] = min(tree[2 * idx][1], tree[2 * idx + 1][1])

        baskets_tree = segmentTree(baskets_idx)

        count = 0
        for fruit in fruits:
            # binary search baskets_idx which: basket[i] >= fruit
            target = bisect.bisect_left(baskets_idx, (fruit, -1))
            baskets_tree = updateTree(N, baskets_tree, target, INF)
            if target < N:
                # baskets[target] = INF
                count += 1
            print("target", target, baskets_tree)
        return count

fruits = [4,2,5]
baskets = [3,5,4]
print(fruits, baskets)

x = Solution()
y = x.numOfUnplacedFruits(fruits, baskets)