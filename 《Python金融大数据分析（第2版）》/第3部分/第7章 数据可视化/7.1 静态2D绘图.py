import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns # seaborn是一个基于matplotlib的绘图库，提供了一些更高级的绘图功能和样式
import numpy as np

# 检查版本
print("Matplotlib version:", mpl.__version__)

# 设置Seaborn主题
sns.set_theme(style="darkgrid")  # 可换成: darkgrid, whitegrid, ticks, etc.

# 设置中文字体
mpl.rcParams['font.sans-serif'] = ['STSong']  # 宋体
mpl.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# 示例数据
x = np.arange(1, 9)
y1 = np.array([100, 110, 90, 105, 95, 115, 120, 130])
y2 = np.array([80, 85, 95, 90, 100, 105, 110, 115])

# 创建绘图
plt.figure(figsize=(10, 6))
plt.plot(x, y1, marker='o', linestyle='-', color='b', label='方案A')
plt.plot(x, y2, marker='s', linestyle='--', color='r', label='方案B')

# 标题和坐标轴
plt.title("不同方案下的指标变化示意图")
plt.xlabel("时间（天）")
plt.ylabel("指标值")

# 显示网格和图例
plt.grid(True)
plt.legend()

# 显示图形
plt.show()
