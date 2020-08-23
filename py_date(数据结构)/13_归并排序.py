# 归并排序
# 最优时间复杂度
# 最坏时间复杂
# 稳定性：稳定

def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    # left 采用归并排序后形成的有序的新的列表
    left = merge_sort(alist[:mid])
    # right 采用归并排序后形成的有序的新的列表
    right = merge_sort(alist[mid:])
    # 将两个有序的子序列合并为一个新的列表
    left_cursor,right_cursor = 0,0
    result = []
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            result.append(left[left_cursor])
            left_cursor += 1
        else:
            result.append(right[right_cursor])
            right_cursor += 1
    result += left[left_cursor:]
    result += right[right_cursor:]
    print('n')
    return result

alist = [54,31,93,17,77,26,44,55,20]
sort_alist = merge_sort(alist)
print('排序前：',alist)
print('排序后：',sort_alist)