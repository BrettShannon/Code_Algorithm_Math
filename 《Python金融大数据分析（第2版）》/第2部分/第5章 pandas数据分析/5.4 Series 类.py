import pandas as pd
import matplotlib.pyplot as plt  # 替换 from pylab import plt
import numpy as np

plt.rcParams['font.family'] = ['serif']  # 设置全局字体

np.random.seed(100)
a = np.random.standard_normal((9, 4)) # 生成9行4列的随机数
df = pd.DataFrame(a, columns=['No1', 'No2', 'No3', 'No4']) # 将数组a转换为DataFrame对象, columns定义列名
df.index = pd.date_range('2019-1-1', periods=9, freq='M') # 定义行索引

print(type(df)) # 打印df的类型

S = pd.Series(np.linspace(0, 15, 7), # Series是pandas库中的一种数据结构, 可以看作是带标签的一维数组
              name='series') # 生成一个Series对象, linspace函数生成0到15之间的7个数, name定义Series对象的名称
print('\n')
print(S)

print('\n')
print(type(S))

print('\n')

s = df['No1']
print(s)

print('\n')
print(type(s))

print(s.mean())

print('\n')
s.plot(lw=2.0, figsize=(10, 6)) # 绘制s的折线图, lw定义线宽, figsize定义图形大小
plt.show()