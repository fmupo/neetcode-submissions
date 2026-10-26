class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        maximum_profit =0
        for i in prices:
            if min_price > i:
                min_price = i
            else:
                current_profit = i- min_price
                if maximum_profit < current_profit:
                    maximum_profit = current_profit
        return maximum_profit


