#urllib(url处理模块)
# 导入request模块(打开和读取url)


#1.urllib库的使用
import urllib.request
# 2.设定访问的目标地址
url = 'https://www.i4.cn/wper_1_1_0_1.html'

#3.开始进行网络链接，发送请求，接受数据
# urlopen()函数用于实现对目标url的访问
html = urllib.request.urlopen(url)

# 4.读取访问网络返回的数据
data = html.read()

# 5.存储在本地
#open()函数，用于打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
# wb是以二进制的格式打开一个文件进行写入，如果该文件存在，打开并清空内容，重新写入。
# 如果没有，创建新文件
# 缓存 0为不寄存 1为寄存
file = open('爱思助手.html','wb')

# 6.写入数据
file.write(data)

#7.关闭文件
file.close()









