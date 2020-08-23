



# alist = [1,5,6,4,2,3]
# new_list = []
# k = 0
#
# for i in range(len(alist)):
#     if alist[i] < 2 or alist[i] > 4:
#         alist[k] = alist[i]
#         k += 1
#
# print(alist[:k])

# import numpy as np
#
# print('%.20f'%(1 / np.log10(1.8062)))

# 删除列表中重复的元素，使表中所有元素的值均不同
# alist = [1,2,2,3,3,3,4,5,6,6,6,6]
# def func(l):
#     # 第一种方法，适用于所有语言
#     k = 0
#     n = len(l)
#     for i in range(1,n):
#         if l[i] != l[i-1]:
#             l[k] = l[i-1]
#             k += 1
#     l[k] = l[i]
#     return l[:k+1]
#     # 第二种方法，python独有一行代码解决
#     # return [i for i in set(l)]
#
# print(func(alist))



# 最少时间内查找有序列表中的元素，如果存在则与后继元素位置相交换，没有则将其插入表中并依旧保持有序。
# alist = [1,2,3,5,6]
# def func_search(alist,num):
#     left,right = 0,len(alist)-1
#     while left <= right:
#         mid = (left + right) // 2
#         if alist[mid] == num and mid != len(alist)-1:
#             alist[mid],alist[mid+1] = alist[mid+1],alist[mid]
#             return alist
#         elif alist[mid] < num:
#             left = mid + 1
#         else:
#             right = mid - 1
#     if mid != len(alist) -1:
#         alist.insert(left,num)
#     return alist
#
# print(func_search(alist,6))

# 求两个升序序列的中位数

# alist1 = [11,13]
# alist2 = [8,20]
#
# def search_middle_num(alist1,alist2):
#     '''此函数用来求两个等长升序序列的中位数'''
#     first1,last1,first2,last2 = 0,len(alist1)-1,0,len(alist2)-1
#
#     while first1 != last1 or first2 != last2 :
#         m1 = (first1 + last1) // 2
#         m2 = (first2 + last2) // 2
#
#         if alist1[m1] == alist2[m2]:
#             return alist1[m1]
#         elif alist1[m1] < alist2[m2]:
#             if (first1 + last1) % 2 == 0: # alist1中元素个数为奇数
#                 first1,last2 = m1,m2
#             else:
#                 first1,last2 = m1 + 1,m2
#         else:
#             if (first2 + last2) % 2 == 0:  # alist2中元素个数为奇数
#                 last1,first2 = m1,m2
#             else:
#                 last1,first2 = m1,m2 + 1
#
#     return min(alist1[first1],alist2[first2])
#
# print(search_middle_num(alist1,alist2))

# import csv
# alist = [["Top Gun","Risky Business","Minority Report"],
#          ["Titanic","The Revenant","Inception"],
#          ["Training Day","Man on Fire","Flight"]]
#
# with open("test1.csv","w",encoding="utf-8") as file_obj:
#     obj = csv.writer(file_obj,delimiter="",lineterminator='\n')
#     for al in alist:
#         obj.writerow(al)

# class Rectangle():
#     def __init__(self,l,w):
#         self.len = l
#         self.width = w
#     def area(self):
#         return self.len * self.width
#     def change_size(self,w,l):
#         self.width = w
#         self.len = l
#
#
# MyRectangle = Rectangle(12,11)
# print(MyRectangle.area())
# MyRectangle.change_size(11,11)
# print(MyRectangle.area())

# alist = [1,2,5,6]
# for i in alist.copy():
#     print(alist.pop())





