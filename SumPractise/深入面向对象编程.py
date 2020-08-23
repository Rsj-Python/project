# 在Python中，类即对象
# Python中的每个类，都是type类的一个实例对象

# class Square():
#     pass
# print(Square) #<class '__main__.Square'>

# 类中有两种类型的变量：类变量和实例变量
# 类变量属于Python为每个类定义创建的对象，以及类本身创建的对象。类变量定义方式与普通变量相同
# (接上：但是必须在类内部定义)
# 类变量可以在不使用全局变量的情况下，在类的所有实例之间共享数据
# 例子
class Shape():
    res = []
    def __init__(self,l,w):
        self.width = w
        self.len = l
        self.res.append([self.len,self.width])

my_shape1 = Shape(2,3)
my_shape2 = Shape(4,5)
my_shape3 = Shape(7,8)
print(Shape.res)








