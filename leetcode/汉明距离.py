class Solution():
    def hammingDistance(self,x,y):
        return bin(x ^ y).count('1')
my = Solution()
print(my.hammingDistance(1,4))