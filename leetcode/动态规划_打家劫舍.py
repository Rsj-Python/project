class Solution():
    def rob(self,nums):
        if nums == []:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        for i in range(2,len(nums)):
            nums[i] += max(nums[:i-1])
        return max(nums)
my = Solution()
print(my.rob([2,1,1,2]))