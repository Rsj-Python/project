class Solution():
    def climbStairs(self,n):
        new_list = [1,2]
        for i in range(2,n):
            new_list.append(new_list[i-1] + new_list[i-2])
        return new_list[n-1]
my = Solution()
