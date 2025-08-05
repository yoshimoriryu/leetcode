class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        idx = 0
        if len(s) == len(t):
            n = len(s)
            while idx < n:
                if s[idx] in s_dict:
                    s_dict[s[idx]] = s_dict[s[idx]] + 1
                else:
                    s_keyval = {s[idx]: 1}
                    s_dict.update(**s_keyval)
                
                if t[idx] in t_dict:
                    t_dict[t[idx]] = t_dict[t[idx]] + 1
                else:
                    t_keyval = {t[idx]: 1}
                    t_dict.update(**t_keyval)
                idx = idx + 1

            return s_dict == t_dict
        else:
            return False

    # short, but not better speed + mem
    def isAnagram1(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t

    def printAnswer(self, answer):
        print(answer)

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    x = Solution()
    x.printAnswer(x.isAnagram(s,t))
