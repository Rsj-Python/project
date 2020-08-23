import numpy as np
# 创建一个数组
array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])# 3行3列的数组
print(array)

array = np.arange(24).reshape(4,6)# arange()类似于range()函数，reshape()用来决定数组的形状
print(array)
# 得到数组的维度数
n = array.ndim
print(n)
# 得到数组的维数
n = array.shape
print(n)
# 得到数组元素的个数
n = array.size
print(n)
# 创建全0数组
array = np.zeros((3,3),dtype=int)# 创建了一个3行3列的全0数组，默认位浮点数可通过dtype=int修改为整形
print(array)
# 创建全1数组
array = np.ones((2,3,3),dtype=int)# 创建了一个含有2个3行3列的全1的3维数组，同样可通过dtype=int修改为整形
print(array)
# 创建随机数数组
array = np.random.rand(2,2)# 创建了一个2行2列范围在[0,1)的2维数组
print(array)

array = np.random.randn(2,2)# 创建了一个2行2列范围是标准正态分布的2维数组
print(array)

array = np.random.randint(1,20,size=(4,4))#创建了一个范围在[1,20)的4行4列的2维数组
print(array)

array = np.random.randint(1,20,size=(2,3,3))#创建了一个范围在[1,20)的2个3行3列的3维数组
print(array)
# 数组索引
array = np.arange(12).reshape(2,3,2)
print(array,array[0,1,1])# 访问数组中的元素时可以将索引写进一个中括号里面
# 数组运算
# 数组的加减乘除以及乘方运算方式为，相应位置的元素分别进行运算。
array1 = np.array([10,30,40,50])
array2 = np.arange(1,5)
print(array1,array2)
print(array1 / array2)# 对应位置上的数字相除
print(array1 - array2)# 对应位置上的数字相减
print(array2**2)# 对应位置上的数字做2次幂
print(array1 * array2)# 对应位置上的数字做乘积(以上运算法则适用于二维数组)
array3 = np.array([[2,4],[3,0]])
print(array3.sum())# 数组中的元素求和
print(array3.min())# 数组中的最小的那个元素
print(array3.max())# 数组中最大的元素
# 数组的平均值
print(np.mean(array))
# 数组方差
print(np.var(array))
# 数组标准差
print(np.std(array))
# 数组最大值与最小值
print(np.min(array),np.max(array))
# 改变数组维度
# reshape函数：不改变原数组维度，有返回值
# resize函数：直接改变原数组维度，无返回值
# shape属性：直接改变原数组维度
array = np.arange(12)
print(array.reshape(2,6),array)
print(array.resize(2,6),array)
array.shape = (2,6)
print(array)
# ravel & flatten 将数组变为一维
array = np.arange(12).reshape(2,3,2)
print(array,array.ravel(),array.flatten())
# 创建矩阵
# Numpy的矩阵对象与数组对象相似，主要不同之处在于，矩阵对象的计算遵循矩阵数学运算规律。
# 矩阵使用matrix函数创建
mat_rix = np.matrix([[1,2],[3,4]])
print(mat_rix)
# 矩阵运算
# 转置
print(mat_rix.T)
# 乘法
mat_rix1 = np.mat([[1,2],[4,5]])
print(mat_rix * mat_rix1)
# 逆矩阵
print(mat_rix.I)
# 数组转置(行变列)
# transpose函数或者array.T
array = np.arange(12).reshape(3,4)
print(array)
print(array.transpose(),array.T)
# 数组的合并
array1 = np.arange(9).reshape(3,3)
array2 = array1 * 2
# 水平合并
print(np.hstack((array1,array2)))
# 垂直合并
print(np.vstack((array1,array2)))
# 深度合并
print(np.dstack((array1,array2)))
# 数组的拆分
array = np.arange(9).reshape(3,3)
# 水平拆分
print(np.hsplit(array,3))
# 垂直拆分
print(np.vsplit(array,3))
# 深度拆分
array = np.arange(18).reshape(3,3,2)
print(np.dsplit(array,2))


