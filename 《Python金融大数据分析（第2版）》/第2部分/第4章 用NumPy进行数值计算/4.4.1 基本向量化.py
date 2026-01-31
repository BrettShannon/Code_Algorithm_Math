# 将两个NumPy数组按元素相加：

import numpy as np

np.random.seed(100) # 设置随机数种子 # seed函数的作用是设定随机数种子，使得每次运行程序时生成的随机数序列都是一样的。

# 创建一个4x3的数组：
# 这样做是为了确保代码的可重复性。

r = np.arange(12).reshape((4, 3)) # 创建一个4x3的数组，从0开始，步长为1，到12结束（不包括12）。
s = np.arange(12).reshape((4, 3)) * 5 # 创建一个4x3的数组，从0开始，步长为5，到12结束（不包括12）。
                            # 步长为5，表示每隔5个元素取一个元素，即每隔5个元素取一个元素，得到一个形状为(4, 3)的数组。
# reshape函数用于改变数组的形状，参数-1表示自动计算该维度的大小。

print(r)
print('\n')
print(s)
print('\n')
print(r + s)
print('\n')

print(r + 3)
print('\n')

print(2 * r)
print('\n')

print(2 * r + 3)

print('\n')

print(r.shape) # 返回数组的形状，即(4, 3)。
print('\n')

s = np.arange(0, 12, 4) # 创建一个数组，从0开始，步长为4，到12结束（不包括12）。
print(s)
print('\n')

print(r + s)
print('\n')

s = np.arange(0, 12, 3) # 创建一个数组，从0开始，步长为3，到12结束（不包括12）。
print(s)
print('\n')

# print(r + s) # r和s的形状不匹配，无法进行按元素相加操作。(r的形状是(4, 3)，s的形状是(4,)，无法进行按元素相加操作。)

print(r.transpose() + s) # r的转置形状是(3, 4)，s的形状是(4,)，可以进行按元素相加操作。
# transpose()函数用于转置数组，即将数组的行和列互换。
print('\n')

sr = s.reshape(-1, 1) # 将s的形状变为(4, 1)。
print(sr)
print('\n')
print(sr.shape)
print('\n')

print(r + s.reshape(-1, 1)) # r的形状是(4, 3)，s的形状是(4, 1)，可以进行按元素相加操作。
print('\n')


def f(x):
    return 3 * x + 5

print(f(0.5))
print('\n')

print(f(r))
