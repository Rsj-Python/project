class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new = []
        for i in nums1:
            if i in nums2:
                new.append(i)
                nums2.remove(i)
        return new
my = Solution()
print(my.intersect([1,2,2,1],[2]))