# 最长回文串好代码版
class Solution():
    def longestPalindrome(self,s):
        beg,flag = 0,0
        for i in set(s):
            if s.count(i) % 2 != 0:
                beg += 1
                flag = 1
        count = len(s) - (beg - flag)
        return count
my = Solution()
print(my.longestPalindrome('abccccdd'))