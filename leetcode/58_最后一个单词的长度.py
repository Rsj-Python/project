



class Solution():
    def lengthOfLastWord(self,s):
        '''常规版本'''
        count = 0
        s = s.rstrip(' ')
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i] != ' ':
                count += 1
            else:
                break
        return count
    def lengthOfLastWord2(self,s):
        '''四行代码版本'''
        s = s.rstrip(' ')
        if len(s) != 0:
            return len(s.split()[-1])
        else:
            return 0

my = Solution()
print(my.lengthOfLastWord('Hello World '))
