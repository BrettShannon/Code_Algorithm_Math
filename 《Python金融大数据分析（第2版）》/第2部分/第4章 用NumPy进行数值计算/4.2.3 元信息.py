import numpy as np

g = np.arange(15) # 生成0-14的数组

print(g.size) # 15
# size表示数组中元素的个数

print(g.itemsize) # 8
# itemsize表示每个元素的字节数

print(g.ndim) # 1
# ndim 表示数组的维度

print(g.shape) # (15,)
# shape表示数组的形状

print(g.dtype) # int64
# dtype表示数组的元素类型

print(g.nbytes) # 120
# nbytes表示数组总字节数

# nbytes = itemsize * size
# 8 * 15 = 120