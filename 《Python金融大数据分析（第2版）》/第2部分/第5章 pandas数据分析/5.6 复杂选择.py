import pandas as pd
import numpy as np

data = np.random.standard_normal((10, 2))# 生成10行2列的随机数

df = pd.DataFrame(data, columns=['x', 'y'])# 将数据转换为DataFrame格式

print(df) # 查看数据

'''

print(df.info())# 查看数据的基本信息

print('\n')

print(df.head())# 查看数据的前几行

print('\n')

print(df.tail())# 查看数据的后几行

print('\n')

print(df) # 查看整个数据

print('\n')
'''

'''
print(df['x'] > 0.5)# 查看x列中大于0.5的元素
print('\n')

print(df['x'] > 0 & (df['y'] < 0)) # 查看x列中大于0且y列中小于0的元素
print('\n')

print(df['x'] > 0 | (df['y'] < 0)) # 查看x列中大于0或y列中小于0的元素
'''

'''
print(df[df['x'] > 0]) # 查看x列中大于0的元素
print('\n')

print(df.query('x > 0')) # 查看x列中大于0的元素 
# query()函数可以接受一个字符串作为参数，该字符串可以包含任意的布尔表达式
# query()函数的意思是，查看x列中大于0的元素
print('\n')

print(df[(df['x'] > 0) & (df['y'] < 0)]) # 查看x列中大于0且y列中小于0的元素
print('\n')

print(df.query('x > 0 & y < 0')) # 查看x列中大于0且y列中小于0的元素
print('\n')

print(df[(df.x > 0) | (df.y < 0)]) # 查看x列中大于0或y列中小于0的元素
print('\n')
'''

print(df > 0) # 判断所有元素是否大于0
print('\n')

print(df[df > 0]) # 查看所有元素中大于0的元素
print('\n')
# print(df > 0) 和 print(df[df > 0]) 的区别在于，前者返回的是布尔值，后者返回的是满足条件的元素