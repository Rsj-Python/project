# 三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，
# 计算小孩有多少种上楼梯的方式。


class Solution():
    '''三步问题'''
    def waysToStep(self,n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        one,two,thr = 4,2,1
        for i in range(4,n+1):
            one,two,thr = (one + two + thr),one,two
        return one
my = Solution()
print(my.waysToStep(40))




