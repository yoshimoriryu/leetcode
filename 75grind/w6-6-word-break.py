from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = {}
        for val in wordDict:
            wd[val] = 0

        while s:
            for k,v in wd.items():
                if k in s:
                    s.replace(k, "")
                wd[k] += 1
        
        for _,v in wd.items():
            if v == 0:
                return False
        return True

s = "leetcode"
wordDict = ["leet", "code"]
x = Solution()
print(x.wordBreak(s,wordDict))