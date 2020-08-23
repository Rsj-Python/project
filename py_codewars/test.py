# l = [1,2,2,2,3]
# for i in range(l.count(2)):
#     l.remove(2)
# print(l)
# a = '12345'
# b = "".join(sorted(str(a), reverse=True))
# print(b)
# l = [1,2,3,4,5]
# def fn(list):
#     for i in range(0,len(l)):
#         if list[i] == 3:
#             return i
# print(fn(l))
# s = 'My name is Tom !'
# l1 = s.split()
# l2 = []
# end_list = []
# print(l1)
# for i in range(len(l1)):
#     l2.append(list(l1[i]))
# print(l2)
# for i in range(len(l2)):
#     l2[i].append(l2[i][0])
#     l2[i].pop(0)
#     a = ''.join(l2[i])
#     end_list.append(a)
# print(end_list)
# for i in range(len(end_list)):
#     end_list[i] = end_list[i]+'ay'
# print(' '.join(end_list))
# l = [1,2,3,4,5,6]
# print(l[0:0])
# l = ['Hello','world']
# print(list(' '.join(l)))
# d1 = {'name':'rsh','age':18}
# d2 = {'name':'shao','age':18}
# for i in d1.keys():
#     print(d1[i])
# print(list('hello'))
# s = 'aabb'
# print(s[1:])
# s = 'Are *they here *'
# s1 = (s.replace(' ',''))
# print(s1)
# strs = ["flower","flow","flight"]
# result = ""
# for temp in zip(*strs):
#     if len(set(temp)) == 1:
#         result += temp[0]
#     else:
#         break
# print(result)
# for i in zip(*strs):
#     print(i)
# print(ord('a'))
# print(ord('z'))
# print(ord('A'),ord('Z'))
from pylab import *
import matplotlib.pyplot as pl
mpl.rcParams['font.sans-serif'] = 'FangSong'
mpl.rcParams['axes.unicode_minus'] = False
# 2D效果
# 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
figure(figsize=(8, 6), dpi=80)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
plot(X, S, color="green", linewidth=1.0, linestyle="-")

# 设置横轴的上下限
xlim(-4.0, 4.0)

# 设置横轴记号
xticks(np.linspace(-4, 4, 9, endpoint=True))

# 设置纵轴的上下限
ylim(-1.0, 1.0)

# 设置纵轴记号
yticks(np.linspace(-1, 1, 5, endpoint=True))

# 以分辨率 72 来保存图片
savefig("0001png", dpi=72)

# 在屏幕上显示
# 获取当前坐标轴对象
ax = gca()
# 一共有上下左右四条边框，设定2个边框为无色none,然后移动另外边框的位置，形成坐标轴
# 设定右边框为无色
ax.spines['right'].set_color('none')
# 设定上边框为无色
ax.spines['top'].set_color('none')
# 将水平坐标的刻度置于底边框（X轴下边）
ax.xaxis.set_ticks_position('bottom')
# 以底边框为X轴，将其置于数据坐标的原点
ax.spines['bottom'].set_position(('data',0))
# 将垂直坐标的刻度置于左边框（Y轴左边）
ax.yaxis.set_ticks_position('left')
# 以左边框为Y轴，将其置于数据坐标的原点
ax.spines['left'].set_position(('data',0))
show()





















