

# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

class Solution():
    def lengthOfLongestSubstring(self,s):
        occ = set()
        ans = 0
        st = 0
        # 遍历每个字符，做为回文串的开头
        n = len(s)
        for i in range(n):
            # 每搜索完一个字符，滑动窗口右移一位,集合移除前一个字符
            if i > 0:
                occ.remove(s[i - 1])
            # 搜索无重复子串，改变窗口大小
            while st < n and s[st] not in occ:
                occ.add(s[st])
                st = st + 1
            ans = max(ans, len(occ))
        return ans
my = Solution()
print(my.lengthOfLongestSubstring("advds"))