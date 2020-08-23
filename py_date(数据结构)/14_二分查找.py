# 二分查找(递归与非递归版本)

def binary_search1(alist,item):
    '''二分查找，递归'''
    n = len(alist)
    if n >= 1:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search1(alist[:mid],item)
        else:
            return binary_search1(alist[mid+1:],item)
    return False
def binary_search2(alist,item):
    '''二分查找，非递归'''
    n = len(alist)
    first,last = 0,n-1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return False

if __name__ == '__main__':
    alist = [17,20,26,31,44,54,55,77,93]
    print(binary_search1(alist,20))
    print(binary_search1(alist,78))
    print(binary_search2(alist, 20))
    print(binary_search2(alist, 78))






