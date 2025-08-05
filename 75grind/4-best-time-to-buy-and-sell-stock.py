from typing import List

class Solution:
    # mine, TLE
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        while prices:
            low = min(prices)
            low_idx = prices.index(low)

            high = -1
            for price in prices[low_idx+1:]:
                if price > high:
                    high = price
            if max_profit < high - low:
                max_profit = high - low
            prices.pop(low_idx)
        return max_profit

    def maxProfit1(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_profit = 0
        while j < len(prices):
            print(i, j)
            if prices[i] >= prices[j]:
                i = j
            else:
                val = prices[j] - prices[i]
                print(val)
                max_profit = max(max_profit, val)
            j = j + 1
        return max_profit

    def printAnswer(self, answer):
        print(answer)

if __name__ == "__main__":
    prices = [7,2,51,3,1,6,4]
    x = Solution()
    x.printAnswer(x.maxProfit1(prices))
