import numpy as np

a = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11],
              [12, 13, 14, 15]])
# np.array()作用是创建一个数组，参数是一个二维列表，表示一个4行4列的二维数组。

print(type(a))
print()

print(a.nbytes) # nbytes: 4 * 4 * 4 = 64 bytes,nbytes作用是计算数组a占用的内存空间大小
print()

print(a.sum()) # .sum()作用是计算数组a中所有元素的和
print()

print(a.cumsum(axis=0)) # .cumsum(axis=0)作用是计算数组a中每一列元素的和
print()

print(a + a)
print()

print(a * 2)
print()

print(sum(a)) # sum()作用是计算数组a中所有元素的和
print()

print(np.sum(a)) # np.sum()作用是计算数组a中所有元素的和
print()

print(a.__sizeof__()) # __sizeof__()作用是计算数组a占用的内存空间大小
print()

# 以下是书上没有的：
print(a.shape) # shape作用是返回数组a的形状，即行数和列数
print()

print(a.size) # size作用是返回数组a中元素的个数
print()

print(a.dtype) # dtype作用是返回数组a中元素的类型
print()

print(a.ndim) # ndim作用是返回数组a的维度，即数组的维数
print()

print(a.itemsize) # itemsize作用是返回数组a中每个元素占用的字节数
print()

print(a.T) # T作用是返回数组a的转置，即行和列互换
print()
# 以下是书上没有的，但是很有用的：
print(a[0, 1]) # a[0, 1]作用是返回数组a中第0行第1列的元素
print()

print(a[0, :]) # a[0, :]作用是返回数组a中第0行的所有元素
print()

print(a[:, 1]) # a[:, 1]作用是返回数组a中第1列的所有元素
print()

print(a[0:2, 1:3]) # a[0:2, 1:3]作用是返回数组a中第0行到第1行，第1列到第2列的所有元素
print()

# ……