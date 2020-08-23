# 动态规划算法之整数拆分
# 难度：中等
# 题目：给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
class Solution():
    def integerBreak(self,n):
        # dp[i]表示将数字i分割(至少分割成两部分)后得到的最大乘积
        dp = [-1] * (n+1)
        dp[1] = 1
        for i in range(2,n+1):
            # 求解dp[i]
            for j in range(1,i):
                # 每一次尝试将i分割成j + (i-j) 两部分
                dp[i] = max(dp[i],j*(i-j),j*dp[i-j])
        return dp[n]
my = Solution()
print(my.integerBreak(9))