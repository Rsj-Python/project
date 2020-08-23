class Solution():
    def removeElement(self,nums,val):
        for i in nums.copy():
            if i == val:
                nums.remove(val)
        return len(nums)
my = Solution()
print(my.removeElement([0,1,2,2,3,0,4,2],2))