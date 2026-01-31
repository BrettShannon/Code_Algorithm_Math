import numpy as np
import matplotlib.pyplot as plt

strike = np.linspace(50, 150, 24) # 行权价
ttm = np.linspace(0.5, 2.5, 24) # 到期时间
strike, ttm = np.meshgrid(strike, ttm) 
# 行权价和到期时间网格,用于计算隐含波动率曲面, 即隐含波动率曲面上的每个点对应一个行权价和到期时间,
# 即隐含波动率曲面上的每个点对应一个隐含波动率,即隐含波动率曲面上的每个点对应一个期权价格,
# meshgrid()函数将两个一维数组转换为二维数组,即生成一个二维网格,用于计算隐含波动率曲面

print(strike[:2].round(1)) # 打印行权价网格的前两行,即前两个行权价
print()

iv = (strike - 100) ** 2 / (100 * strike) / ttm 
# 隐含波动率曲面,即隐含波动率曲面上的每个点对应一个隐含波动率
# 隐含波动率曲面上的每个点对应一个期权价格,即隐含波动率曲面上的每个点对应一个隐含波动率
print(iv[:5, :3]) # 打印隐含波动率曲面的前五行和前三列,即前五个到期时间和前三个行权价的隐含波动率


from mpl_toolkits.mplot3d import Axes3D # 导入3D绘图模块
'''
fig = plt.figure(figsize=(10, 6))
ax = fig.gca(projection='3d') # 创建3D绘图对象
surf = ax.plot_surface(strike, ttm, iv, rstride=2,
                       cstride=2, cmap=plt.cm.coolwarm,
                       linewidth=0.5, antialiased=True) # 绘制隐含波动率曲面

ax.set_xlabel('Strike') # 设置x轴标签
ax.set_ylabel('Time to maturity') # 设置y轴标签
ax.set_zlabel('Implied volatility') # 设置z轴标签

fig.colorbar(surf, shrink=0.5, aspect=5) # 添加颜色条

plt.show() # 显示绘图


Traceback (most recent call last):
  File "/Users/mac/Documents/✏️学习记录：编程、算法、数学/《Python金融大数据分析（第2版）》/第3部分/第7章 数据可视化/7.2 静态3D绘图.py", line 23, in <module>
    ax = fig.gca(projection='3d') # 创建3D绘图对象
TypeError: FigureBase.gca() got an unexpected keyword argument 'projection'

这个错误是因为您使用的Matplotlib版本较新，gca() 方法的语法发生了变化。在新版本中，创建3D坐标轴的正确方式是使用 add_subplot() 方法。
'''

'''
# 创建画布和3D坐标轴
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')  # 修正这里 # 原代码：ax = fig.gca(projection='3d')
# 111表示创建一个1行1列的子图，并选择第一个子图，projection='3d'表示创建3D坐标轴

# 假设有一些示例数据（您需要替换为实际数据）
# strike = ... # 您的行权价数据
# ttm = ...    # 您的到期时间数据  
# iv = ...     # 您的隐含波动率数据


# 绘制隐含波动率曲面
surf = ax.plot_surface(strike, ttm, iv, rstride=2,
                       cstride=2, cmap=plt.cm.coolwarm,
                       linewidth=0.5, antialiased=True)

ax.set_xlabel('Strike')
ax.set_ylabel('Time to maturity') 
ax.set_zlabel('Implied volatility')

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

# 👆 完美 😍
# 但是上面这段知识涉及数学，我还没有学，以后再说
'''

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(30, 60) # 设置视角
ax.scatter(strike, ttm, iv, zdir='z', s=25, c='b', marker='o') # 绘制散点图
ax.set_xlabel('Strike')
ax.set_ylabel('Time to maturity')
ax.set_zlabel('Implied volatility')
plt.show()