# 1.abs()函数
# abs函数用来返回数字的绝对值
print(abs(-23))

# 2.range()函数
# range()函数可以生成一个列表
print(list(range(5)))#会输出[0,1,2,3,4]不包括最后一个数字5,也可以传进去两个参数,会返回一个列表从第一个参数开始,最后一个参数前一个数字结束

# 3.bin()函数 oct()函数 hex()函数
# bin()函数用来将十进制转换为二进制
print(type(bin(10))) # 类型为字符型
print(bin(10))
# oct()函数用来将十进制转换为八进制
print(type(oct(10))) # 类型为字符型
print(oct(10))
# hex()函数用来将十进制转换为十六进制
print(type(hex(10))) # 类型为字符型
print(hex(10))
# 其他进制转换为十进制
print(int('1010',2)) # 二进制转换为十进制
print(int('12',8)) # 八进制转换为十进制
print(int('a',16)) # 十六进制转换为十进制

# 4
