class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new_nums = set(nums)
        return len(new_nums) != len(nums)
mc = Solution()
print(mc.containsDuplicate([2,14,18,22,22]))