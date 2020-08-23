# 力扣第十五题
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
# 请你找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 示例：给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
class Solution():
    def threeSum(self,nums):
        if len(nums) < 3:
            return []
        n = len(nums)
        new_nums = []
        for i in range(0,n):
            for j in range(i+1,n-1):
                c = 0 - nums[i] - nums[j]
                if c in nums[j+1:]:
                    new_nums.append(sorted([nums[i],nums[j],c]))

        new_nums1 = list(map(lambda i:list(i),list(set([tuple(t) for t in new_nums]))))
        return new_nums1
my = Solution()
print(my.threeSum([1,2,-2,-1]))





















