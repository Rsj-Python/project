import random

# randint()方法，可随机生成一个整数

# 随机生成一个0 - 100 之间的整数
print(random.randint(0,100))

# choice方法，适用于随机取列表中的值
alist = ["北京","天津","上海","苏州"]
print(random.choice(alist))