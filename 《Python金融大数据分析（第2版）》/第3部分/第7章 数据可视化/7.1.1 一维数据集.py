import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1000) # 设置随机种子,1000为随机数种子

y = np.random.standard_normal(20) # 生成20个服从标准正态分布的随机数
print(y)
print()

x = np.arange(len(y)) # 生成0到19的整数序列,len(y)表示y的长度, 即20, arange函数用于生成指定范围的整数序列
print(x)
print()


print(x.shape,y.shape) # 打印x,y的形状
# 输出(20,) (20,) ：# 表示x,y都是一维数组,长度为20

'''
plt.plot(x,y) # 绘制散点图
# plot英文意思： 可与draft和diagram换用，但侧重于表示具体的点、面、部分或目标，从而使相互关系以及和整体的关系得以明确
plt.show() # 显示图形
'''

'''
plt.plot(y.cumsum()) # 绘制y的累积和；# cumsum英文意思： 累积和,音标： [ˈkjuːməs]
plt.grid(False) # 不显示网格
plt.axis('equal') # 设置坐标轴比例相等； ；axis英文意思： 轴，音标： [ˈæksɪs]

plt.show() # 显示图形
'''


'''
plt.plot(y.cumsum()) # 绘制y的累积和；# cumsum英文意思： 累积和,音标： [ˈkjuːməs]
plt.xlim(-1, 20) # 设置x轴的范围

# 设置y轴的范围
plt.ylim(np.min(y.cumsum()) -1, # .min(y.cumsum()) -1意思： y的累积和的最小值减1
         np.max(y.cumsum()) + 1) # .max(y.cumsum()) + 1意思： y的累积和的最大值加1

plt.show() # 显示图形
'''


# 标签：
'''
plt.figure(figsize=(10, 6)) # 设置图形大小
plt.plot(y.cumsum(), 'b', lw=1.5) # 绘制y的累积和；'b'表示蓝色；lw=1.5表示线宽为1.5
plt.plot(y.cumsum(), 'ro') # 绘制y的累积和；'ro'表示红色圆点
plt.xlabel('index') # 设置x轴标签
plt.ylabel('value') # 设置y轴标签
plt.title('A Simple Plot') # 设置图形标题
plt.show() # 显示图形
# plot的英文意思是绘制，音标： [plɒt]
'''
