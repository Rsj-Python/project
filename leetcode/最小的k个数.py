class Solution():
    def getLeastNumbers(self,arr,k):
        arr.sort()
        return arr[:k]
my = Solution()
print(my.getLeastNumbers(arr = [3,2,1], k = 2))