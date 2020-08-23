# 选择排序
# 最优时间复杂度O(n^2)
# 最坏时间复杂度O(n^2)
# 稳定性：不稳定(考虑升序每次选择最大的情况)
def select_sort(alist):
    n = len(alist)
    for i in range(n-1):
        mix_index = i
        for j in range(i+1,n):
            if alist[mix_index] > alist[j]:
                mix_index = j
        alist[i],alist[mix_index] = alist[mix_index],alist[i]


alist1 = [54,26,93,17,77,31,44,55,20]
alist2 = [1,3,2,4,5,6,7]
print('排序前:',alist1)
select_sort(alist1)
print('排序后:',alist1)
print('排序前:',alist2)
select_sort(alist2)
print('排序后:',alist2)




