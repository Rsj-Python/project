# 动态规划算法之三角形最小路径和
# 难度：中等
# 题目：给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
class Solution():
    def minimumTotal(self,triangle):
        '''主要思路：triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])'''
        n = len(triangle)
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]
l = [
       [2],
      [3,4],
     [6,5,7],
    [4,1,8,3]
    ]
my = Solution()
print(my.minimumTotal(l))