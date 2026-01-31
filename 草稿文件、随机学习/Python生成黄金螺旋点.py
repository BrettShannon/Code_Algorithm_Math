import numpy as np
import matplotlib.pyplot as plt

phi = (1 + np.sqrt(5)) / 2  # 黄金比例

def fibonacci_spiral_points(n_points=1000):
    theta = np.linspace(0, 4 * np.pi, n_points)
    r = phi ** (theta / (2 * np.pi))  # 指数螺旋
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

x, y = fibonacci_spiral_points()
plt.plot(x, y)
plt.axis('equal')
plt.show()
