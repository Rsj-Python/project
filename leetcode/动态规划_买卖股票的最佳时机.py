class Solution():
    def maxProfit(self,prices):
        if len(prices) == 0:
            return 0
        new_list = [0 for i in range(len(prices))]
        for i in range(1,len(prices)):
            dif = prices[i] - prices[i-1]
            if dif + new_list[i-1] < 0:
                new_list[i] = 0
            else:
                new_list[i] = dif + new_list[i-1]
        return max(new_list)
my = Solution()
print(my.maxProfit([7,1,5,3,6,4]))