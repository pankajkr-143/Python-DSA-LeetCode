# Question : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

solution = Solution()

prices = [7,1,5,3,6,4]
print(solution.maxProfit(prices))  # Output: 5

prices = [7,6,4,3,1]
print(solution.maxProfit(prices))  # Output: 0

prices = [1, 2]
print(solution.maxProfit(prices))  # Output: 1