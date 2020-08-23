class Solution():
    def twoSum(self,nums,target):
        result = []
        for i in nums:
            if (target - i) in nums:
                if i == target - i and nums.count(i) > 1:
                    result.append(nums.index(i))
                    result.append(nums.index(target - i, nums.index(i) + 1))
                    break
                elif i != target - i:
                    result.append(nums.index(i))
                    result.append(nums.index(target - i))
                    break
        return result
my = Solution()
print(my.twoSum([1,2,3,6,8],10))