# 散点图

import numpy as np
import matplotlib.pyplot as plt

y = np.random.standard_normal((1000, 2)) # 生成1000个二维数据点
'''
plt.figure(figsize=(10, 6)) # 设置画布大小,figsize意思是宽和高，单位是英寸，1英寸=2.54厘米

plt.plot(y[:, 0], y[:, 1], 'ro') # 绘制散点图，'ro'表示红色圆点,y[:, 0], y[:, 1]表示x轴和y轴的数据
plt.xlabel('1st') # 设置x轴标签
plt.ylabel('2nd')  # 设置y轴标签
plt.title('Scatter plot')  # 设置标题
plt.show()  # 显示图形
'''


# plt.scatter()函数 绘制散点图
'''
plt.figure(figsize=(10, 6)) # 设置画布大小,figsize意思是宽和高，单位是英寸，1英寸=2.54厘米
plt.scatter(y[:, 0], y[:, 1], marker='o') # 绘制散点图，marker='o'表示使用圆点
plt.xlabel('1st') # 设置x轴标签
plt.ylabel('2nd')  # 设置y轴标签
plt.title('Scatter plot')  # 设置标题
plt.show()  # 显示图形
'''


c = np.random.randint(0, 10, len(y)) # 生成0-10之间的随机整数，长度与y相同
'''
plt.figure(figsize=(10, 6)) # 设置画布大小,figsize意思是宽和高，单位是英寸，1英寸=2.54厘米
plt.scatter(y[:, 0], y[:, 1], c=c,  # scatter函数功能包括：绘制散点图，设置颜色映射，设置标记类型等
            cmap='coolwarm',
            marker='o')
             # 绘制散点图，c=c表示使用c作为颜色映射，
             # cmap='coolwarm'表示使用coolwarm颜色映射，marker='o'表示使用圆点，
plt.colorbar() # 添加颜色条
plt.xlabel('1st') # 设置x轴标签
plt.ylabel('2nd')  # 设置y轴标签
plt.title('Scatter plot')  # 设置标题
plt.show()  # 显示图形
'''
# 直方图：
'''
plt.figure(figsize=(10, 6)) # 设置画布大小,figsize意思是宽和高
plt.hist(y, label=['1st', '2nd'], bins=25) # 绘制直方图，bins=25表示将数据分成25个区间
plt.legend(loc=0) # 添加图例
plt.xlabel('value') # 设置x轴标签
plt.ylabel('frequency')  # 设置y轴标签
plt.title('Histogram')# 设置标题
plt.show()  # 显示图形
'''

# 两个数据集的数据在直方图中堆叠：
'''
plt.figure(figsize=(10, 6)) # 设置画布大小,figsize意思是宽和高
plt.hist(y, label=['1st', '2nd'], color=['b', 'g'], stacked=True, bins=20) 
                    # 绘制直方图，bins=25表示将数据分成25个区间,stacked=True表示堆叠
plt.legend(loc=0) # 添加图例
plt.xlabel('value') # 设置x轴标签
plt.ylabel('frequency')  # 设置y轴标签
plt.title('Histogram')# 设置标题
plt.show()  # 显示图形
'''

# 箱线图：
fig, ax = plt.subplots(figsize=(10, 6)) # 设置画布大小,fig和ax 是两个变量，fig是画布，ax是坐标轴
plt.boxplot(y) # 绘制箱线图
plt.setp(ax, xticklabels=['1st', '2nd']) 
        # 设置x轴标签,xticklabels=['1st', '2nd']表示x轴标签是'1st'和'2nd'
plt.xlabel('data set') # 设置x轴标签
plt.ylabel('value')  # 设置y轴标签
plt.title('Box plot')# 设置标题
plt.show()  # 显示图形


# 🧀️🧀️🧀️ plt.setp()函数，这一节涉及数学，不懂，以后再说
