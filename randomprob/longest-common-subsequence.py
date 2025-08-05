# failed to solve; revisit count: 1
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
 
        m,n = len(text2), len(text1)
        i,j = 0,0
        count = 0
        while i < m and j < n:
            print(text2[i], text1[j])
            if text2[i] == text1[j]:
                count += 1
                i += 1
            j += 1
            if j == n and count == 0:
                j = 0
                i += 1

        count2 = 0
        i,j = 0,0
        while i < m and j < n:
            print(text2[i], text1[j])
            if text2[i] == text1[j]:
                count2 += 1
                j += 1
            i += 1
            if i == m and count == 0:
                i = 0
                j += 1
        
        return max(count,count2)

# memoization; top-down DP
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]