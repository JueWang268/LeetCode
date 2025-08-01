
class Solution:
    def maxProfit(self, k:int, prices: List[int]) -> int:

        # using two DP arrays
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54125/Very-understandable-solution-by-reusing-Problem-III-idea
        profit = 0

        # case 1: no possible profit because of insufficient # of days
        # or transactions
        if k == 0 or len(prices) <= 1:
            return 0

        # case 2: k is large enough to buy and sell every day
        # essentially no constraint. Just add all the upticks together
        if 2*k >= len(prices):
            for i in range(1, len(prices)):
                # compare price to previous day
                # if it goes up, keep looking out for more profit
                if prices[i] >= prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # case 3: anything else
        # use two DP arrays to keep track of max profit possible to buy/sell
        # on each transaction, and update based on the previous day's value


        profitDP = [0 if i%2 == 1 else -float("inf") for i in range(2*k)]
        # we always want to buy on the first day to get things started
        profitDP[0] = -prices[0]

        for d in range(len(prices)): # day number
            for t in range(2*k): # transaction numebr
                if t == 0:
                    # special case for first day cuz we always want to update 
                    # initial buying price
                    profitDP[t] = max(profitDP[t], -prices[d])
                elif t % 2 == 1: #should be selling, or holding
                    profitDP[t] = max(profitDP[t], profitDP[t- 1] + prices[d])
                else: # should be buying, or holding
                    profitDP[t] = max(profitDP[t], profitDP[t-1] - prices[d])
        
        return profitDP[2*k - 1]