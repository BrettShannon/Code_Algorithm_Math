import pandas as pd
import matplotlib.pyplot as plt  # 替换 from pylab import plt # pyplot是matplotlib的子库，用于绘制各种图表
import numpy as np

plt.rcParams['font.family'] = ['serif']  # 设置全局字体，
                            # rcParams是matplotlib的配置参数字典，font.family表示字体族，serif表示衬线字体

np.random.seed(100) # 设置随机种子，使得每次运行代码时生成的随机数相同
                    # random()函数生成0到1之间的随机数，seed()函数设置随机种子
                    # 100表示随机种子为100,随机种子的意思是每次运行代码时生成的随机数相同
a = np.random.standard_normal((9, 4)) # 生成9行4列的随机数
df = pd.DataFrame(a, columns=['No1', 'No2', 'No3', 'No4']) # 将数组a转换为DataFrame对象, columns定义列名
df.index = pd.date_range('2019-1-1', periods=9, freq='M') # 定义行索引


# 添加一列，表示对应缩阴数据所属的季度：
df['Quater'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3'] # 添加新列

print(df)
print('\n')

groups = df.groupby('Quater') # 按照Quater列分组，groupby()函数返回一个GroupBy对象，该对象表示按指定列分组的数据
print(groups.size()) # 查看每个分组的大小
print('\n')

print(groups.mean()) # 查看每个分组的均值
print('\n')

print(groups.max()) # 查看每个分组的最大值
print('\n')

print(groups.aggregate([min,max]),round(2)) # 查看每个分组的最大值和最小值，并保留两位小数,
                # aggregate()函数可以接受一个函数列表作为参数

# 添加另一列，表示索引日期的月份是奇数还是偶数：

df['OddEven'] = ['Odd', 'Even', 'Odd', 'Even','Odd', 'Even', 'Odd', 'Even', 'Odd'] # 添加新列
groups = df.groupby(['Quater', 'OddEven']) # 按照Quater和OddEven列分组
print(groups.size()) # 查看每个分组的大小
print('\n')

print(groups[['No1', 'No4']].aggregate([sum, np.mean])) # 查看每个分组的No1和No4列的和和均值
print('\n')