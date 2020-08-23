class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in nums.copy():
            if i == 0:
                nums.append(i)
                nums.remove(i)
        print(nums)
my = Solution()
my.moveZeroes([0,1,0,3,12])