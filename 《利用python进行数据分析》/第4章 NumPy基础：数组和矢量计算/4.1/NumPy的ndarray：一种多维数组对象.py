import numpy as np

'''
data = np.random.randn(2, 3)
# 使用 NumPy 来生成一个 2 行 3 列的随机数数组
# 其中每个数值都是从 标准正态分布（均值为 0，标准差为 1） 中随机抽取的。

print(data)

a = data * 10
print(a)

b = data + data
print(b)

c = data.shape
print(c)
# shape 表示各维度大小的元祖

d = data.dtype
print(d)
# dtype用于说明数组数据类型的对象
'''

# 创建ndarray
'''
data_1 = [6, 7.5, 8, 0, 1]
arr_1 = np.array(data_1)

print(arr_1)

data_2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr_2 = np.array(data_2)

print(arr_2)

print(arr_2.ndim)
print(arr_2.shape)
print(arr_1.dtype)
print(arr_2.dtype)
'''

print(np.zeros(10))
print(np.zeros((3, 6)))

print(np.arange(15))

