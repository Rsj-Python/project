# 凯撒密码的实现
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
class CaesarPassword():
    # 加密
    def Encryption(self,str):
        '''实现恺撒密码的加密'''
        print('加密后：',end='')
        for s in str:
            if s in ['x','y','z']:
                print(chr(ord(s)-23),end='')
            else:
                print(chr(ord(s)+3),end='')
        print()
    # 解密
    def Decrypt(self,str):
        '''实现恺撒密码的解密'''
        print('解密后：',end='')
        for s in str:
            if s in ['a','b','c']:
                print(chr(ord(s)+23),end='')
            else:
                print(chr(ord(s)-3),end='')
        print()
my = CaesarPassword()

while True:
    print('*'*15,'欢迎使用恺撒密码！','*'*15)
    print('1.加密')
    print('2.解密')
    print('3.退出')
    choice = input('请输入您想要做的操作：(1\\2\\3)')
    print('*'*47)
    if choice == '1':
        s = input('请输入明文：')
        my.Encryption(s)
    elif choice == '2':
        s = input('请输入密文：')
        my.Decrypt(s)
    elif choice == '3':
        exit()
    else:
        print('您的输入有误，请重新输入！')



