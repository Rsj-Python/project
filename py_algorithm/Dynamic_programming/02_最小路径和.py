# 动态规划算法之最小路径和
# 难度：中等
# 题目：给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
class Solution():
    def minPathSum(self,grid):
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]
grid = [
  [1]
]
my = Solution()
print(my.minPathSum(grid))