from typing import List
import math

# failed to solve
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        dp=[math.inf] * (amount+1)
        dp[0]=0
    
        print(dp)
        for coin in coins:
            for i in range(coin, amount+1):
                print('ini i', i)
                if i-coin>=0:
                    print(dp[i], dp[i-coin]+1)
                    dp[i]=min(dp[i], dp[i-coin]+1)
        
        return -1 if dp[-1]==math.inf else dp[-1]

coins = [1,3,5]
amount = 6
x = Solution()
print(x.coinChange(coins, amount))