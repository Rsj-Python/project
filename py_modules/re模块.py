# re模块，与正则表达式联系比较密切

import re

# findall方法，将正则表达式和目标文本作为参数传入，该方法将以列表形式返回文本中与正则表达式匹配的所有元素
I = "Beautiful is better than ugly."
maches = re.findall("beautiful",I,re.IGNORECASE) # re.IGNORECASE作为第三个参数传入，可忽略大小写
print(maches)

# 使用补字符的例子
zen = """Although never is
oftern better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!
"""
m = re.findall("^If",zen,re.MULTILINE) # 传入re.MULTILINE作为findall的第三个参数，才能在
# 多行文本中找到所有匹配的内容
print(m)

# 在正则表达式中加入[abc],则可匹配a、b、或c
string = 'Two too.'
m = re.findall("t[ow]o",string,re.IGNORECASE) # 方括号中为o,w.则匹配too 或者 two
print(m)

# 可使用 \d 匹配字符串中的数字
line = "123?34 hello?"
m = re.findall("\d",line,re.IGNORECASE)
print(m)

# 在正则表达式中，句号可以匹配任意字符。如果在句号后加一个星号，这将让正则表达式匹配任意字符零或多次
t = "__one__ __two__ __three__"
found = re.findall("__.*?__",t) # 加一个 ? ,表示非贪婪匹配，不加问号会直接匹配一行
print(found)

# 在正则表达式中的字符前加上一个反斜杠\即可进行转义
line = "I love $ very much"
m = re.findall("\$",line,re.IGNORECASE) #如果没有反斜杠则什么也匹配不到
print(m)







