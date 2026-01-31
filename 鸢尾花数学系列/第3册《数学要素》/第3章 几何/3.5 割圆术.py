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
    fig, ax = plt.subplots() #
    ax.set_aspect('equal')
    hexagon_inner = RegularPolygon((0, 0), numVertices=num_vertices, 
                                   radius=1, orientation=np.pi/2, alpha=0.2, edgecolor='k')
    ax.add_patch(hexagon_inner)
    hexagon_outer = RegularPolygon((0, 0), numVertices=num_vertices,
                               radius=1, orientation=np.pi/num_vertices, 
                               alpha=0.2, edgecolor='k')
    ax.add_patch(hexagon_outer)
    circle = Circle((0, 0), radius=1, edgecolor='k', facecolor='none')
    ax.add_patch(circle)

    plt.axis('off')

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.show()