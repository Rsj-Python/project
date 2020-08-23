# 插入排序
# 最优时间复杂度：O(n)
# 最坏时间复杂度：O(n^2)
# 稳定性：稳定

def insert_sort(alist):
    n = len(alist)
    for i in range(1,n):
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
            else:
                break
alist1 = [54,26,93,17,77,31,44,55,20]
alist2 = [2,1]
print('排序前:',alist1)
insert_sort(alist1)
print('排序后:',alist1)
print('排序前:',alist2)
insert_sort(alist2)
print('排序后:',alist2)











