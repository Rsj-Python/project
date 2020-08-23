class Solution(object):
    def maxProfit(self, prices):
        i = count = 0
        j = 1
        while j <= len(prices):
            try:
                if prices[j] < prices[j-1]:
                    count += (prices[j-1] - prices[i])
                    i = j
                    j += 1
                elif prices[j] >= prices[j-1]:
                    j += 1
            except:
                count += (prices[j-1]-prices[i])
                j += 1
        return count
mysolution = Solution()
print(mysolution.maxProfit([7,1,5,3,6,4]))





















