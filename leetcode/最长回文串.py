class Solution():
    def longestPalindrome(self,s):
        if s == '':
            return 0
        elif len(set(s)) == 1:
            return len(s)
        else:
            count = 0
            flag = True
            for i in set(s):
                if s.count(i) % 2 == 0:
                   count += s.count(i)
                elif s.count(i) % 2 == 1:
                    count += s.count(i) - 1
                    flag = False
            if flag:
                return count
            else:
                return count + 1
my = Solution()
print(my.longestPalindrome('cccc'))