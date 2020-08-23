#
#
#
# def reverse_list(l):
#     '''
#
#     :param l:list
#     :return: l
#     '''
#     i,j = 0,len(l) - 1
#     while i < j:
#         l[i],l[j] = l[j],l[i]
#         i += 1
#         j -= 1
#     return l
#
# def max_and_min(l):
#     '''
#
#     :param l: list:l
#     :return: min and max
#     '''
#     min,max = l[0],l[0]
#     for i in range(1,len(l)):
#         if min > l[i]:
#             min = l[i]
#         elif max < l[i]:
#             max = l[i]
#     return {"最小值":min,"最大值":max}
#
# def merge_dlist(list1,list2):
#     '''
#     [1,2,3,5]   [4,6,7,8,9]
#     :param l:list1 与 list2 为两个升序列表
#     :return: 合并后的列表
#     '''
#     new_list = []
#     i,j = 0,0
#     while i != len(list1) and j != len(list2):
#         if list1[i] < list2[j]:
#             new_list.append(list1[i])
#             i += 1
#         else:
#             new_list.append(list2[j])
#             j += 1
#     if i < len(list1):
#         new_list += list1[i:]
#     if j < len(list2):
#         new_list += list2[j:]
#     return new_list
# print(reverse_list([3,1,5,9,2]))
# print(max_and_min([3,1,5,9,2]))
# print(merge_dlist([1,5,6,7,8,9],[2,3,4]))
alist = [1,2,3]
