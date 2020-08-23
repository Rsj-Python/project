




class Solution():
    def addBinary(self,a,b):
        '''
        a ，b为二进制字符
        :param a: str
        :param b: str
        :return: 返回 a + b的二进制和
        '''
        return bin(int(a,2) + int(b,2))[2:]
my = Solution()
print(my.addBinary('11','1'))






