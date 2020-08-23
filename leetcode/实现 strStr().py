class Solution():
    def strStr(self,haystack, needle):
        return haystack.find(needle)
        if needle == "":
            return 0
my = Solution()
haystack = ""
needle = "wewe"
print(my.strStr(haystack,needle))