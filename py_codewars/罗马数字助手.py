# 此类用于罗马数字和阿拉伯数字转换
class RomanNumerals():
    def from_roman(self,s):
        '''此函数用来将罗马数字转换为整数'''
        d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
             'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        res, i, j = 0, 0, 2
        if len(s) == 2:
            if d[s[0]] < d[s[1]]:
                return d[s]
            else:
                return d[s[1]] + d[s[0]]
        while i < len(s):
            if s[i:j] in d:      # 'IXX'
                res += d[s[i:j]]
                i = j
                j += 2
            else:
                res += d[s[i]]
                i += 1
                j += 1
        return res
    def to_roman(self,n):
        '''此函数用来将正整数转换为罗马数字'''
        alist = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
                 (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I'),]
        for

my = RomanNumerals()
print(my.from_roman('MCMXCIX'))
print(my.to_roman(3990))

