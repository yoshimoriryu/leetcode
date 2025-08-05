from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        trash_count = 0
        for trash in garbage:
            trash_count += len(trash)
        
        i = len(travel)
        j = i
        p,g,m = 0,0,0
        while j >= 0:
            print(p,g,m)
            if "P" in garbage[j] and not p:
                p = sum(travel[:i])
            if "G" in garbage[j] and not g:
                g = sum(travel[:i])
            if "M" in garbage[j] and not m:
                m = sum(travel[:i])
            if p and g and m:
                break
            i -= 1
            j -= 1
        print(p,g,m, trash_count)
        return p+g+m+trash_count