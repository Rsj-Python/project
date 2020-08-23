class Solution():
    def romanToInt(self,s):
        d = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,
            'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        res,i,j = 0,0,2
        if len(s) == 2:
            if d[s[0]] < d[s[1]]:
                return d[s]
            else:
                return d[s[1]] + d[s[0]]
        while i < len(s):
            if s[i:j] in d:
                res += d[s[i:j]]
                i = j
                j += 2
            else:
                res += d[s[i]]
                i += 1
                j += 1
        return res
my = Solution()
print(my.romanToInt('XII'))