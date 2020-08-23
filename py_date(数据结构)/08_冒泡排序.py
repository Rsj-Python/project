# 冒泡排序
# 最优时间复杂度O(n)
# 最坏时间复杂度O(n^2)
# 稳定性：稳定
def bubble_sort(alist):
    '''冒泡排序'''
    n = len(alist)
    for i in range(1,n):
        count = True
        for j in range(n-i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                count = False
        if count:
            return
alist1 = [54,26,93,17,77,31,44,55,20]
alist2 = [1,2,3,4,5,6,7]
print('排序前:',alist1)
bubble_sort(alist1)
print('排序后:',alist1)
print('排序前:',alist2)
bubble_sort(alist2)
print('排序后:',alist2)