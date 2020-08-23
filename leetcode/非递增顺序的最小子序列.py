# 力扣第1403题


class Solution():
    def minSubsequence(self,nums):
        '''此函数用来求一个数组中非递增顺序的最小子序列'''
        new_nums = []
        nums = sorted(nums,reverse=True)
        for i in nums.copy():
            new_nums.append(i)
            nums.remove(i)
            if sum(new_nums) > sum(nums):
                return new_nums

my = Solution()
nums = [4,3,10,9,8]
print(my.minSubsequence(nums))