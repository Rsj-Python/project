class Solution():
    def isAnagram(self,s,t):
        res = True
        if set(s) != set(t):
            return False
        else:
            for i in set(s):
                res = res and s.count(i) == t.count(i)
            return res
my = Solution()
print(my.isAnagram('abbs','sbab'))