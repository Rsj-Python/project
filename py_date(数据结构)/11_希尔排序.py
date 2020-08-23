# 希尔排序
# 最优时间复杂度：根据步长序列的不同而不同
# 最坏时间复杂度：O(n^2)
# 稳定性：不稳定
def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for i in range(gap,n):
            j = i
            while j >= gap:
                if alist[j] < alist[j-gap]:
                    alist[j],alist[j-gap] = alist[j-gap],alist[j]
                    j -= gap
                else:
                    break
        # 缩短gap步长
        gap //= 2
alist1 = [54,31,93,17,77,26,44,55,20]
alist2 = [7,6,5,4,3,2,1]
print('排序前:',alist1)
shell_sort(alist1)
print('排序后:',alist1)
print('排序前:',alist2)
shell_sort(alist2)
print('排序后:',alist2)






