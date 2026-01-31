import numpy as np

'''
# 一维数组：
g = np.arange(15) # 生成0-14的数组
print(g)
print(g.shape) # (15,) 一维数组

print(np.shape(g)) # (15,) 一维数组

g = g.reshape(3, 5) # 重新定义数组形状
print(g)

h = g.reshape(5, 3) # 重新定义数组形状
print(h)

print(h.T) # 转置
# .T的作用是转置，即把数组的行和列进行互换

print(h.transpose()) # 转置
# transpose()和.T作用相同，都是转置
'''

# 二维数组：
g = np.arange(15) # 生成0-14的数组
h = g.reshape(5, 3) # 重新定义数组形状
print(h)

print(h.flatten()) 
# flatten()的作用是将多维数组转换为一维数组

print(h.flatten(order='C')) # order='C'表示按行优先转换

print(h.flatten(order='F')) # order='F'表示按列优先转换

for i in h.flat:
    print(i, end=',') # end=''表示不换行

for i in h.ravel(order='C'): # ravel()和flatten()作用相同，都是将多维数组转换为一维数组
    print(i, end=',')

for i in h.ravel(order='F'): 
    print(i, end=',')