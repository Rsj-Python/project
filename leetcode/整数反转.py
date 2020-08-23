class Solution():
    def reverse(self,s):
        if s == 0:
            return 0
        x = ''
        if str(s)[0] == '-':
            x += '-'
        x += str(s)[-1::-1].lstrip('0').rstrip('-')
        x = int(x)
        if -2**31 < x < 2**31-1:
            return x
        return 0
my = Solution()
print(my.reverse(-1230))