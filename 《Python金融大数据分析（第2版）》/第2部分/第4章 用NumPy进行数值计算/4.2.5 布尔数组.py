import numpy as np

g = np.arange(15) # 生成0-14的数组
h = g.reshape(5, 3) # 重新定义数组形状

print(h)
print('\n') 

'''
print(h > 8) # 比较数组元素是否大于8
print('\n') 


print(h <= 7) # 比较数组元素是否小于等于7
print('\n') 


print(h == 5) # 比较数组元素是否等于5

print('\n') 

print((h > 4) & (h <= 12)) # 比较数组元素是否大于4且小于等于12
print('\n') 
'''

'''
print(h[h > 8]) # 输出数组元素大于8的元素
print('\n')
print(h[(h > 4) & (h <= 12)]) # 输出数组元素大于4且小于等于12的元素
# & 且
print('\n')
print(h[(h < 4) | (h >= 12)]) # 输出数组元素小于4或大于等于12的元素
# | 或
'''
a = np.where(h > 7, 1, 0) # 将数组元素大于7的元素赋值为1，小于7的元素赋值为0
# np.where(condition, x, y) 如果满足条件，则返回x，否则返回y

print(a)
print('\n')

b = np.where(h % 2 == 0, 'even', 'odd') # 将数组元素为偶数的元素赋值为'even'，奇数的元素赋值为'odd'
print(b)
print('\n')

c = np.where(h <= 7, h * 2, h / 2) # 将数组元素小于等于7的元素乘以2，大于7的元素除以2
print(c)

