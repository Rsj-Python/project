import numpy as np
import matplotlib.pyplot as pl
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
# 1.绘制正弦曲线，并设置标题、坐标轴名称、坐标轴范围
x = np.arange(0,2*np.pi,0.01)
y = np.sin(x)
pl.plot(x,y)
# 设置标题
pl.title('正弦函数',fontdict={'size':20})
# 设置x轴名称
pl.xlabel('弧度',fontdict={'size':15})
# 设置y轴名称
pl.ylabel('正弦值',fontdict={'size':15})
# 设置坐标轴范围
pl.axis([-0.07*np.pi,2.07*np.pi,-1.07,1.07])
pl.show()
# 2.同一坐标系中绘制多种曲线并通过样式、宽度、颜色加以区分
x = np.linspace(-4,4,200)
f1 = np.power(10,x)
f2 = np.power(np.e,x)
f3 = np.power(2,x)
pl.plot(x,f1,'b',ls='-',lw=2,label='$10^x$')# 设置f1函数的样式、宽度和颜色
pl.plot(x,f2,'g',ls='--',lw=2,label='$e^x$')# 设置f2函数的样式、宽度和颜色
pl.plot(x,f3,'r',ls=':',lw=2,label='$2^x$')# 设置f3函数的样式、宽度和颜色
pl.axis([-4,4,-0.5,10])
pl.text(1,9.5,r'$10^x$',fontsize=16)
pl.text(2.4,9.5,r'$e^x$',fontsize=16)
pl.text(3.4,9.5,r'$2^x$',fontsize=16)
pl.title(u'幂函数曲线',fontdict={'size':20})
pl.xlabel(u'横坐标',fontdict={'size':15})
pl.ylabel(u'纵坐标',fontdict={'size':15})
pl.legend(loc='lower right')
pl.show()
# 3.绘制多轴图，即将多幅子图绘制在同一画板
# 在左上角绘制余弦函数
pl.subplot(221)
x = np.arange(0,2*np.pi,0.01)
f1 = np.cos(x)
pl.plot(x,f1,'r',lw=2)
pl.title(u'余弦函数',fontdict={'size':10})
# 在右上角绘制正弦函数
pl.subplot(222)
x = np.arange(0,2*np.pi,0.01)
f2 = np.sin(x)
pl.plot(x,f2,'y',lw=2)
pl.title(u'正弦函数',fontdict={'size':10})
# 在正下方绘制e^x函数
pl.subplot(212)
x = np.linspace(-4,4,200)
f3 = np.power(np.e,x)
pl.plot(x,f3,'b',lw=2)
pl.title(u'$e^x$函数',fontdict={'size':10})
pl.show()
# 4.直方图的绘制(数据自己定义)
# ①频数直方图
pl.subplot(211)
data= np.random.normal(0,1,2000)
pl.hist(data,20,color='y')
pl.title(u'频数直方图')
# ②频率直方图
pl.subplot(212)
pl.hist(data,20,density=True,color='k')
pl.title(u'频率直方图')
pl.show()
# 5.绘制散点图
x = np.random.rand(50)
y = np.random.rand(50)
color = np.random.rand(50)
s_value = 200 * x
pl.scatter(x,y,s=s_value,c=color)
pl.title(u'散点图')
pl.xlabel('X')
pl.ylabel('Y')
pl.show()
# 6.绘制盒状图
data = np.random.randn(1000)
fig,ax = pl.subplots(1,figsize = (8,4))
ax.boxplot(data)
pl.show()