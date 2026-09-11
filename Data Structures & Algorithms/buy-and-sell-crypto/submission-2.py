class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxim = 0
        for l in range(len(prices)-1):
            r=l+1

            while r<len(prices) and prices[l] < prices[r]:
                diff = prices[r] - prices[l]

                maxim = max(maxim,diff) 
                print(maxim,diff)
                r+=1
        return maxim
            
            


        
        