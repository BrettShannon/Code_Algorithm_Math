import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon, Circle # 导入正多边形和圆形
import numpy as np
# 割圆术
# 割圆术是古希腊数学家阿基米德提出的一种计算圆周率的方法。它基于将圆分割成许多小正多边形，然后计算这些正多边形的周长，从而逼近圆的周长。
# 割圆术的基本思想是将圆分割成许多小正多边形，然后计算这些正多边形的周长，从而逼近圆的周长。具体来说，我们可以将圆分割成许多小正多边形，然后计算这些正多边形的周长，从而逼近圆的周长。
# 割圆术的基本步骤如下：
# 1. 将圆分割成许多小正多边形，例如正方形、正六边形、正十二边形等。
# 2. 计算每个小正多边形的周长，然后将这些周长相加，得到整个圆的近似周长。
# 3. 通过增加小正多边形的数量，可以逐渐逼近圆的周长。

# 割圆术的Python代码实现如下：

for num_vertices in [6, 8, 10, 12, 14, 16]: # 正多边形的边数
    fig, ax = plt.subplots()            # figure和axes对象,他们的意思是“图形”和“轴”
    ax.set_aspect('equal')               # 设置坐标轴比例相等，使图形为圆形
    hexagon_inner = RegularPolygon((0, 0),
                                   numVertices=num_vertices,
                                   radius=1, orientation=np.pi/2,
                                   alpha=0.2, edgecolor='k')
    # 上面的代码创建了一个正多边形，其中心在(0,0)，边数为num_vertices，半径为1，方向为np.pi/2，透明度为0.2，边框颜色为黑色。
    # RegularPolygon函数的参数解释如下：
    # (0, 0)：正多边形的中心坐标。
    # numVertices：正多边形的边数。
    # radius：正多边形的半径。
    # orientation：正多边形的初始方向，以弧度为单位。
    # alpha：正多边形的透明度，取值范围为0到1。
    # edgecolor：正多边形的边框颜色。
    # facecolor：正多边形的填充颜色。
    # linewidth：正多边形的边框宽度。
    # linestyle：正多边形的边框样式。

    ax.add_patch(hexagon_inner)
    hexagon_outer = RegularPolygon((0, 0),
                                   numVertices=num_vertices,
                                   radius=1, orientation=np.pi/num_vertices,
                                   alpha=0.2, edgecolor='k')
    
    ax.add_patch(hexagon_outer)  # 添加正多边形到图形中，
    circle = Circle((0, 0), radius=1, edgecolor='k', facecolor='none')
    # 创建一个圆形，其中心在(0,0)，半径为1，边框颜色为黑色，填充颜色为无。
    ax.add_patch(circle) # 添加圆形到图形中

    plt.axis('off')  # 关闭坐标轴，使图形更美观

    plt.xlim(-1.5, 1.5) # 设置x轴范围
    plt.ylim(-1.5, 1.5) # 
    plt.show()