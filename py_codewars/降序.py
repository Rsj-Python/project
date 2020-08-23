# 您的任务是创建一个可以将任何非负整数作为参数的函数，并以降序返回其数字。
# 本质上，重新排列数字以创建最大可能的数字。
def descending_order(num):
    new_num = ''.join(sorted(str(num),reverse=True))
    return int(new_num)
print(descending_order(24581))


