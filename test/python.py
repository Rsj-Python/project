#coding=utf-8
# 标识符
# 变量
a = 10
# 行和缩进
if True:
    print("正确")

# 数据类型
# 1.浮点型
n = 3.14
#2.字符串
strl = 'This is Tom'

# print(strl)
# print(strl[8])
# print(strl[5:7])
# 格式化字符串 %s  格式化整数%d
# x = 1.112
# y = 1.2210
# print(y-x)
print(f'My name is 卢吊 and my age is {18}')
# 3.列表
list1 = [1,'hello',True]
# print(list1)
# print(list1[1])
# print(list1[1:2])
# 修改
list1[0] = 2
# 添加
list1.append('卢吊')
# 删除
del list1[2]
# print(list1)
# 元组Tuple有序，内部数据不能修改
tup1 = ('卢吊','任少杰',0,'王云蛋','徐浩然')
tup2 = ('王润之','王岩','李鸿政')
# print(tup1)
# print(tup1[0])
# print(tup1[0:3])
tup = tup1 + tup2
print(tup)

# 字典：无序 key
#可以存储任意数据类型，键值对(key:value)
# dic1 = dict(name='张三',gender='男',age=18)
dic1 = {'name':'张三','sex':'男','age':18}
print(dic1)




















