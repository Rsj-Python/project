class Solution():
    def searchInsert(self,nums,target):
        '''常规版本'''
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
        return len(nums)
    def searchInsert2(self,nums,target):
        '''二分搜索版本'''
        left,right = 0,len(nums)-1
        if nums[right] < target:
            return len(nums)
        else:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return left
my = Solution()
print(my.searchInsert2([1,3,5,6], 7))


















