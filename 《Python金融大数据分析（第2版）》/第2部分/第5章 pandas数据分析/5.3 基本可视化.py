'''
import pandas as pd
from pylab import plt, mpl
import numpy as np

mpl.rcParams['font.family'] = ['serif']  # 设置全局字体
%matplotlib inline # 在jupyter notebook中显示图像
# 👆该魔法命令仅在 Jupyter Notebook（.ipynb）中有效，在 .py 文件中会报语法错误。

np.random.seed(100) # 设置随机种子，保证每次运行结果一致
a = np.random.standard_normal((9, 4)) # 生成9行4列的随机数
df = pd.DataFrame(a) # 将数组a转换为DataFrame对象
df.columns = ['No1', 'No2', 'No3', 'No4'] # 定义列名
dates = pd.date_range('2019-1-1',
                      periods=9,
                      freq='M')
df.index = dates # 定义行索引

df.cumsum().plot(lw=2, figsize=(10, 6)) # 绘制累积和曲线图
# cumsum()是DataFrame对象的方法，用于计算累积和
# plot是DataFrame对象的方法，用于绘制曲线图
# lw参数用于设置线宽
# figsize参数用于设置图像大小
print(a) # 打印图像对象
'''

# deepseek修改版:

import pandas as pd
import matplotlib.pyplot as plt  # 替换 from pylab import plt
import numpy as np

plt.rcParams['font.family'] = ['serif']  # 设置全局字体

np.random.seed(100)
a = np.random.standard_normal((9, 4)) # 生成9行4列的随机数
df = pd.DataFrame(a, columns=['No1', 'No2', 'No3', 'No4']) # 将数组a转换为DataFrame对象, columns定义列名
df.index = pd.date_range('2019-1-1', periods=9, freq='M') # 定义行索引

df.cumsum().plot(lw=2, figsize=(10, 6)) # 绘制累积和曲线图 # lw设置线宽, figsize设置图像大小
plt.show()  # 显示图表

# 柱状图：

df.plot.bar(figsize=(10, 6), rot=15) # 绘制柱状图 # figsize设置图像大小, rot设置x轴标签旋转角度
plt.show()
# 替代语法：使用kind参数改变绘图类型：
# df.plot(kind='bar', figsize=(10, 6), rot=15) # 绘制柱状图 # kind参数指定图表类型, figsize设置图像大小, rot设置x轴标签旋转角度

# 折线图：

df.plot.line(figsize=(10, 6)) # 绘制折线图 # figsize设置图像大小
plt.show()

# 箱线图：

df.plot.box(figsize=(10, 6)) # 绘制箱线图 # figsize设置图像大小
plt.show()

# 散点图：

df.plot.scatter(x='No1', y='No2', figsize=(10, 6)) # 绘制散点图 # x和y参数指定x轴和y轴的数据列, figsize设置图像大小
plt.show()

# 直方图：

df.plot.hist(bins=20, figsize=(10, 6)) # 绘制直方图 # bins参数指定直方图的柱子数量, figsize设置图像大小
plt.show()

# 饼图：

df.plot.pie(subplots=True, figsize=(10, 6)) # 绘制饼图 # subplots参数指定是否绘制子图, figsize设置图像大小
plt.show()

# 热力图：

df.plot.heatmap(figsize=(10, 6)) # 绘制热力图 # figsize设置图像大小
plt.show()

# 雷达图：

df.plot.radar(figsize=(10, 6)) # 绘制雷达图 # figsize设置图像大小
plt.show()
