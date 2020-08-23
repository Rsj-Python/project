# 您在此kata中的目标是实现一个差异函数，该函数将从另一个列表中减去一个列表并返回结果。
# 它应该从列表中删除列表a中存在的所有值b。
# array_diff([1,2],[1]) == [2]
# 如果中存在一个值，则b必须从另一个值中删除所有出现的值：
# array_diff([1,2,2,2,3],[2]) == [1,3]
def array_diff(list1,list2):
    if list1 == [] or list2 == []:
        return list1
    else:
        i = 0
        while(i < len(list2)):
            for j in range(list1.count(list2[i])):
                list1.remove(list2[i])
            i += 1
        return list1
print(array_diff([-18,1,2,3], [1,2]))











