class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        new_digits = list(str(int(''.join(str(i) for i in digits)) + 1))

        return [int(i) for i in new_digits]
my = Solution()
print(my.plusOne([1,2,9]))