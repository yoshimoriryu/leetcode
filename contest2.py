import bisect
from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        ans = []
        b_idxs = []
        idx_a = s.find(a)
        idx_b = s.find(b)
        if idx_b != -1: b_idxs.append(idx_b)
        while idx_a != -1:
            print(b_idxs)
            for bi in b_idxs:
                if abs(idx_a-bi) <= k:
                    bisect.insort(ans, idx_a)
                    break
            print(s)
            s = s[:idx_a] + '*'*len(a) + s[idx_a+len(a):]
            print(s)
            s = s[:idx_b] + '*'*len(b) + s[idx_b+len(b):]
            print(s)
            idx_a = s.find(a)
            idx_b = s.find(b)
            if idx_b != -1: b_idxs.append(idx_b)
        return ans

x = Solution()
s = "lahhnlwx"
a = "hhnlw"
b = "ty"
k = 6
print(x.beautifulIndices(s,a,b,k))
