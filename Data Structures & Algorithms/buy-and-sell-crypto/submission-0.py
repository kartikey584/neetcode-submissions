class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        pre = [0] * n
        pre[0] = prices[0]

        for i in range(1,n):
            pre[i] = min(pre[i-1],prices[i])
        result = 0
        for i in range(n):
            
            p = prices[i] - pre[i]
            result = max(result,p)
        
        return result

