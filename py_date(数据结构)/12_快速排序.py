# 快速排序
# 必须要掌握
# 最优时间复杂度：O(nlogn)
# 最坏时间复杂度：O(n^2)
# 稳定性：不稳定
def quick_sort(alist,first,last):
    if first >= last:
        return
    mid_value = alist[first]
    low,high = first,last
    while low < high:
        # high 左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 循环退出时，low == high
    alist[low] = mid_value
    # 对low左边的列表执行快速排序
    quick_sort(alist,first,low-1)
    # 对low右边的列表执行快速排序
    quick_sort(alist,low+1,last)

if __name__ == '__main__':
    alist1 = [54,31,93,17,77,26,44,55,20]
    alist2 = [1,6,3,3,4,7,9,5]
    print('排序前alist1：', alist1)
    print('排序前alist2：', alist2)
    quick_sort(alist1,0,len(alist1)-1)
    quick_sort(alist2,0,len(alist2)-1)
    print('排序后alist1：',alist1)
    print('排序后alist2：',alist2)




