# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
class Solution():
    def convert(self,s,numRows):
        if numRows < 2:
            return s
        alist = [''for i in range(numRows)]
        i,flag = 0,-1
        for z in s:
            alist[i] += z
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return ''.join(alist)
my = Solution()
print(my.convert('LEETCODEISHIRING',4))












