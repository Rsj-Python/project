def tribonacci(list, n):
    # if n == 0:
    #     list.clear()
    #     return list
    # elif n == 1:
    #     return list[0:1]
    # elif n == 2:
    #     return list[0:2]
    # else:
    for i in range(3,n):
        list.append(list[i-1] + list[i-2] + list[i-3])
    return list[:n]
print(tribonacci([1, 1, 1], 0))




















