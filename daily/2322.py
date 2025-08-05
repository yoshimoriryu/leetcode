from typing import List
import collections

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        N = len(nums)

        # nums = [1,5,5,4,11]
        # edges = [[0,1],[1,2],[1,3],[3,4]]
        adj_list = collections.defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # is_ancestor[a][b] = is a an ancestor of b
        is_ancestor = [[False] * N for _ in range(N)]

        # precalculate "isAncestor" cache
        def dfs(node, parent, ancestors):
            for a in ancestors:
                is_ancestor[a][node] = True
            
            for v in adj_list[node]:
                if v != parent:
                    ancestors.append(node)
                    dfs(v, node, ancestors)
                    ancestors.pop()
        
        dfs(0, -1, [])

        # xs[i] = subtree xor sum at node i
        xs = [None] * N

        def dfs2(node, parent, xsum):
            current = nums[node]
            for v in adj_list[node]:
                if v != parent:
                    current ^= dfs2(v, node, xsum)
            xs[node] = current
            return current
        
        dfs2(0,-1,0)

        total = xs[0]
        INF = 10**20
        best = INF
        # try every pair of nodes as the subtree
        # theres two cases:
        # 1. the area is totaly has no intersection
        # 2. some area is inside its parent
        # if case here is considering case above 
        for a in range(1, N):
            for b in range(a + 1, N):
                xa = xs[a]
                xb = xs[b]

                components = []
                if is_ancestor[a][b]:
                    # a is ancestor of b
                    # three components are:
                    # xb, xa-xb, total-xa
                    components = [xb, xa ^ xb, total ^ xa]
                elif is_ancestor[b][a]:
                    # xa, xb-xa, total-xb
                    components = [xa, xb ^ xa, total ^ xb]
                else:
                    # totaly separate; xa, xb, total - xa - xb
                    components = [xa, xb, total ^ xa ^ xb]
                
                components.sort()
                delta = components[-1] - components[0]
                best = min(best, delta)
                print("this is delta", delta, best)
        return best

nums = [1,5,5,4,11]
edges = [[0,1],[1,2],[1,3],[3,4]]
x = Solution()
print(x.minimumScore(nums, edges))