class Solution():
    def isPalindrome(self,x):
        if x < 0:
            return False
        else:
            res,n = 0,x
            while n != 0:
                res = res * 10 + n % 10
                n = n // 10
            if res == x:
                return True
            else:
                return False
my = Solution()
print(my.isPalindrome(1001))