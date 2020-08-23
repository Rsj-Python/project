# 床长人工智能教程
# 第一个人工智能程序
# 识别猫


# 一.加载一些工具库
import numpy as np # 主要用来科学计算，是非常非常常用的一个库
from matplotlib import pyplot as plt # 这个库主要用来画图
import h5py # 这个库是用来加载训练数据集的。我们数据集的保存格式是HDF。Hierarchical Data Format(HDF)
# 是一种针对大量数据进行组织和存储的文件格式。大数据和人工智能行业都用它来保存数据。
import skimage.transform as tf # 这里我们用它来缩放图片

# 人工智能需要很多数据来进行训练，下面这个函数用来加载这些数据
def load_dataset():
    train_dataset = h5py.File('datasets/train_catvnoncat.h5','r') # 加载训练数据
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # 从训练数据中提取出图片的特征数据
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # 从训练数据中提取出图片的特征数据

    test_dataset = h5py.File('datasets/test_catvnoncat.h5','r') # 加载测试数据
    test_set_x_orig = np.array(test_dataset['test_set_x'][:])
    test_set_y_orig = np.array(test_dataset['test_set_y'][:])

    classes = np.array(test_dataset['list_classes'][:]) # 加载标签类别数据，这里的类别只有两种，1代表
    # 有猫，0代表无猫

    train_set_y_orig = train_set_y_orig.reshape((1,train_set_y_orig.shape[0])) # 把数组的维度从(209)
    # 变成(1,209)，这样好方便后面进行计算
    test_set_y_orig = test_set_y_orig.reshape((1,test_set_y_orig.shape[0])) # 从(50)变成(1,50)

    return train_set_x_orig,train_set_y_orig,test_set_x_orig,test_set_y_orig,classes

train_set_x_orig,train_set_y,test_set_x_orig,test_set_y,classes = load_dataset()

