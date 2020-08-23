class Solution():
    def isPalindrome(self,s):
        new_s1 = 'abcdefghijklmnopqrstuvwxyz0123456789'
        new_s2 = ''.join([i for i in s.lower() if i in new_s1])
        if new_s2[0:] == new_s2[len(new_s2)-1::-1]:
            return True
s = "A man, a plan, a canal: Panama"
my = Solution()
print(my.isPalindrome(s))







