class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        print(s)
        if not s:
            return True
        while s:
            n = len(s)
            if s[0] == s[n-1]:
                s = s[1:len(s)-1]
            else:
                return False
            if len(s) == 1:
                return True
        return True

    # short af
    def isPalindrome1(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]

    def printAnswer(self, answer):
        print(answer)

if __name__ == "__main__":
    s = "0p"
    x = Solution()
    x.printAnswer(x.isPalindrome(s))
