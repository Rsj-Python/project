class Solution():
    def countAndSay(self, n):
        d = {1:'1',2:'11'}
        for i in range(3,n+1):
            j = st = 0
            s = ''
            while j < len(d[i-1]):
                if d[i-1][j] != d[i-1][j+1]:
                    s += str(len(d[i-1][st:j+1])) + d[i-1][st]
                    st = j+1
                j += 1
                if j == len(d[i-1])-1:
                    if d[i-1][j] == d[i-1][j-1]:
                        s += str(len(d[i-1][st:j + 1])) + d[i-1][st]
                    else:
                        s += str(len(d[i-1][j:j+1])) + d[i-1][j]
                    break
            d[i] = s
        return d[n]
my = Solution()
print(my.countAndSay(4))
