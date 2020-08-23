class Solution():
    def merge(self,nums1,m,nums2,n):
        nums1[m:m+n] = nums2[:n]
        nums1.sort()
        print(nums1)
my = Solution()
my.merge(nums1 = [1,2,3,0,0,0], m = 3,nums2 = [2,5,6],n = 3)