class Solution():
    def isPowerOfThree(self,n):
        import math
        if n == 0:
            return False
        elif 3**int(round(math.log(abs(n),3),0)) == n:
            return True
        else:
            return False
my = Solution()
print(my.isPowerOfThree(-27))