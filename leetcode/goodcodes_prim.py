# 力扣1.只出现一次的数字好代码版
# (1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums))*2 - sum(nums)
# (2)
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a
# 力扣2.整数反转
class Solution():
    def reverse(self,x):
        num = 0
        new_x = abs(x)
        while new_x != 0:
            num = num * 10 + new_x % 10
            new_x = new_x // 10
        if x < 0:
            if -num > -2**31:
                return -num
            else:
                return 0
        else:
            if num < 2**31-1:
                return num
            else:
                return 0
# 力扣3.字符串中的第一个唯一字符
class Solution:
    def firstUniqChar(self,s):
        dict_s = {}
        for i in range(len(s)):
            if s[i] in dict_s:
                continue
            else:
                if s[i] in s[i+1:]:
                    dict_s[s[i]] = 1
                else:
                    return i
        return -1
# 力扣4.最长公共前缀
class Solution():
    def longestCommonPrefix(self,strs):
        result = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                result += i[0]
            else:
                break
        return result



