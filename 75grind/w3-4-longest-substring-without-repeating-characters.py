class Solution:
    # not using dict sliding window, thats why 
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if len(s) == 1:
            return 1
        max_local, max_global = '',''
        n = len(s)
        i = 0
        anchor = 0
        while i < n:
            if s[i] not in max_local:
                max_local += s[i]
            else:
                if len(max_global) < len(max_local):
                    max_global = max_local
                max_local = ''
                anchor += 1
                i = anchor-1
            i += 1
        return len(max_global) if len(max_global) > len(max_local) else len(max_local)
    
    # sliding window
    def lengthOfLongestSubstring1(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            if s[r] not in seen:
                output = max(output, r-l+1)
            else:
                if seen[s[r]] < 1:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output


x = Solution()
print(x.lengthOfLongestSubstring('aab'))