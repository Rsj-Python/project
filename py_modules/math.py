# 该模块提供了很多有关数学的运算方法
import math

## 一.幂与平方根
# pow(x,y):返回 x 的 y 次方,返回值为浮点数
print(math.pow(2,4))

# ldexp(x,i):返回 x * (2 ** i),返回值为浮点数
print(math.ldexp(2,4))

# sqrt(x):求x的算术平方根
print(math.sqrt(2))

# factorial(x):求x的阶乘
print(math.factorial(5))

# hypot(x,y): 得到 x**2 + y**2 的算术平方根,返回值为浮点数
print(math.hypot(3,4))

## 二.常数e相关
# log2(x):返回以2为底的对数,返回值为浮点数
print(math.log2(256))

# log10(x):返回以10为底的对数,返回值为浮点数
print(math.log10(256))

# log(x,base):两个参数都给定，返回以base为底，x的对数，若只给定x，则返回以e为底x的对数
print(math.log(23))

# log1p(x)：:返回x+1的自然对数(基数为e)的值
print(math.log1p(math.e-1))

## 三.圆相关
# pi：常数π，圆周率
print(math.pi)

# radians:把角度x转换成弧度
print(math.radians(30))
print(30 * math.pi / 180) # 与此效果相同

# degrees:把x从弧度转换成角度
print(math.degrees(0.5))

## 四.三角函数
# sin、cos、tan.math 模块对正三角函数的计算，变量是弧度，所以在计算时需要先将角度转换为弧度
angle = 30
re = math.radians(angle)
print(math.sin(re))
print(math.cos(re))
print(math.tan(angle))

## 五.反三角函数
h = math.asin(0.5) # 反正弦函数
print(math.degrees(h)) # 30.0000000004

h = math.acos(0.5) # 反余弦函数
print(math.degrees(h)) # 60.00000000001

h = math.atan(1) # 反正切函数
print(math.degrees(h)) # 45.0

## 六.双曲正弦、余弦、正切，反双曲正弦、余弦、正切
     # sinh   cosh tanh  asinh  acosh  atanh

## 七.其他

# trunc(x)：返回x的整数部分
print(math.trunc(2.3)) # 2

# ceil(x)：取大于等于x的最小的整数值，如果x是一个整数，则返回x
print(math.ceil(3.5)) # 4

# floor(x)：取小于等于x的最大的整数值，如果x是一个整数，则返回自身
print(math.floor(3.5)) # 3

# fabs(x)：返回x的绝对值
print(math.fabs(-2.3)) # 2.3

# modf(x)：返回由x的小数部分和整数部分组成的元组
print(math.modf(2.44)) #(0.4399999999999995,2.0)

# copysign(x, y)：把y的正负号加到x前面，可以使用0
print(math.copysign(2,-3)) # -2.0

# fmod(x, y)：得到x/y的余数，其值是一个浮点数
print(math.fmod(13,2)) # 1.0

# gcd(x, y)：返回x和y的最大公约数
print(math.gcd(8,100)) # 4

# fsum(x)：对迭代器里的每个元素进行求和操作
print(math.fsum([1, 2, 3, 4]))  # 10.0

# isfinite(x)：如果x不是正无穷大或负无穷大，则返回True,否则返回False
print(math.isfinite(100)) # True

# isinf(x)：如果x是正无穷大或负无穷大，则返回True,否则返回False
print(math.isinf(100)) # False

# isnan(x)：如果x不是数字True,否则返回False
print(math.isnan(1.22222)) # False








