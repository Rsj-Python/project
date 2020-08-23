# 面向对象编程有四大概念：封装、抽象、多态、继承
# 他们共同构成了面向对象编程的四大支柱
# class Shape():
#     def __init__(self,w,l):
#         self.width = w
#         self.len = l
#
#     def print_size(self):
#         print("{} by {}".format(self.width,self.len))
#
# class Square(Shape):
#     def area(self):
#         return self.width * self.len
#     def print_size(self):
#         print("I am {} by {}".format(self.width,self.len))
#
# my_shape = Shape(5,6)
# my_shape.print_size()
# my_square = Square(3,4)
# my_square.print_size()

##组合
class Dog():
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self,name):
        self.name = name

mick = Person("Renshaojie")
stan = Dog("旺财","拉布拉多",mick)
print(stan.owner.name)




















