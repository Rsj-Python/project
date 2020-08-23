# os模块(用于处理文件和目录) re模块(正则表达式操作)
# 1.导入模块
import urllib.request
import re
import os
# 2.访问网络的目标地址
url = 'https://www.i4.cn/wper_1_1_0_1.html'

# 3.申请访问，获取相应
html = urllib.request.urlopen(url)

# getcode(获取当前网页带的状态码，200表示网页正常，403为不正常)
if html.getcode() == 200:
    print('网络访问成功',html.getcode())
    #4.读取返回的数据
    data = html.read()
    #5.存储到本地
    file = open('图片.html','wb',1)
    file.write(data)
    file.close()
else:
    print('访问失败')
#6.解析网络图片，进行下载
def get_data_img():
    #创建正则表达式
    #字符串前加r是为了防止转义字符
    r = r'[a-zA-z]+://[^\s]*.jpg'
    #创建正则表达式模板
    #compile()用于编译正则表达式，生成一个正则表达式对象
    pat = re.compile(r)
    #根据正则表达式模板，进行数据匹配
    #findall()方法能够以列表的形式返回能匹配的子串
    imgurls = re.findall(pat,str(data))
    print(imgurls)
    print(len(imgurls))
    #通过循环遍历下载
    i = 0
    path = r'D:\test\py_02\img'
    #os.path模块主要用于获取文件的属性
    #os.path.exists()函数：如果path存在，返回True。如果不存在，返回False
    if not os.path.exists(path):
        os.makedirs(path)
        print('创建路径成功！')
        pass
    #循环遍历
    for i in range(len(imgurls)):
        #urlretrieve()函数，直接将远程数据下载到本地
        #urlretrieve(url,指定保存的路径)
        print(f'开始下载第{i}张图片')
        urllib.request.urlretrieve(imgurls[i],f'{path}/img_{i}.jpg')







    pass
get_data_img()









