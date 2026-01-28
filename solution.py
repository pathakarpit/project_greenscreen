# Problem: Best time to Buy and Sell Stock
# Difficulty: Medium
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def solve(self, prices):
        if not prices:
            return 0
        
        buy1 = float('inf')
        sell1 = 0
        buy2 = float('inf')
        sell2 = 0
        
        for price in prices:
            # For the first transaction, we minimize the cost to buy and maximize profit from selling
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            
            # For the second transaction, we consider how much we would have earned after buying at a lower price and then selling now (if profitable)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)
        
        return sell2

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))