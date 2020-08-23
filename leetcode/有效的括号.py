class Solution():
    def isValid(self,s):
        dic = {'(':')','[':']','{':'}','!':'!'}
        new_list = ['!']
        for i in s:
            if i in dic:
                new_list.append(i)
            elif dic[new_list.pop()] != i:
                return False
        return len(new_list) == 1
my = Solution()
print(my.isValid('(]'))