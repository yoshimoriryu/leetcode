from typing import List


# failed to solve
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = wordDict
        while wd:
            cp_s = s
            print('=======start')
            while cp_s:
                before = cp_s
                print(cp_s)
                for k in wd:
                    if k in cp_s:
                        cp_s = cp_s.replace(k, " ")
                print('sini', before, cp_s, wd)
                if cp_s == before:
                    wd = wd[1:]
                    break
                if not cp_s.strip():
                    return True
        print(cp_s)
        return False

s = "ccaccc"
wordDict = ["cc", "ac"]
x = Solution()
print(x.wordBreak(s,wordDict))