
# 本题用来将整数转换为罗马数字


class Solution():
    def intToRoman(self,num):
        alist = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
                 (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        new_alist = []

        for arab,roman in alist:
            if num == 0:
                break
            count,num = divmod(num,arab)
            new_alist.append(count * roman)

        return ''.join(new_alist)
my = Solution()
print(my.intToRoman(20))
