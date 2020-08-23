# 计算1! + 2! + ······ n!的阶乘
# n = int(input())
# def Factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * Factorial(n-1)
# new_list = []
# for i in range(1,n+1):
#     new_list.append(Factorial(i))
# print(sum(new_list))
s1 = input()
s2 = input()
l = []
for i in range(0,len(s1),8):
    l.append(s1[i:i+8].ljust(8,'0'))
for i in range(0,len(s2),8):
    l.append(s2[i:i+8].ljust(8,'0'))
print(l)