#编写一个函数，该函数以整数作为输入，并返回该数字的二进制表示形式中等于1的位数。
#您可以保证输入为非负数。
def countBits(n):
    num_list = []
    while n != 0:
        num_list.append(n % 2)
        n = n // 2
    return num_list.count(1)

num = int(input('请输入一个大于0的数：'))
if num < 0:
    print('输入有误，重新输入')
else:
    print(countBits(num))