class Solution():
    def missingNumber(self,nums):
        '''
        :param nums:List[int]
        :return:0-len(nums)范围内缺失的数字
        '''
        new_list = list(range(0,len(nums)+1))
        return sum(new_list) - sum(nums)
my = Solution()
print(my.missingNumber([9,7,6,5,4,3,2,1,0]))