class Solution():
    def maxSubArray(self,nums):
        new_list = [0 for i in range(len(nums))]
        new_list[0] = nums[0]
        for i in range(1,len(nums)):
            new_list[i] = max(new_list[i-1] + nums[i],nums[i])
        return max(new_list)
my = Solution()
print(my.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))