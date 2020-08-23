class Solution():
    def isRectangleOverlap(self,rec1,rec2):
        if rec2[0] >= rec1[2] or rec2[3] <= rec1[1] or rec2[2] <= rec1[0] or rec2[1] >= rec1[3]:
            return False
        else:
            return True
my = Solution()
print(my.isRectangleOverlap([-6,-10,9,2],[0,5,4,8]))