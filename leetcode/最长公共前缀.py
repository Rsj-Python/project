class Solution():
    def longestCommonPrefix(self,strs):
        if strs == []:
            return ''
        i = 0
        new_list1 = [[] for i in range(len(strs))]
        new_list2 = []
        while i < min(len(s) for s in strs):
            for j in range(len(strs)):
                new_list1[j].append(strs[j][i])
            new_list2 = [''.join(s) for s in new_list1]
            if len(set(new_list2)) == 1:
                pass
            elif len(set(new_list2)) != 1 or len(set(new_list2)) == len(new_list2):
                return new_list2[0][:i]
            i += 1
        try:
            return new_list2[0]
        except:
            return ''
my = Solution()
strs = ['a']
print(my.longestCommonPrefix(strs))
