class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums = nums[len(nums)-k:] + nums[:len(nums)-k]
        print(nums)
mysolution = Solution()
mysolution.rotate([1,2,3,4,5,6,7],3)