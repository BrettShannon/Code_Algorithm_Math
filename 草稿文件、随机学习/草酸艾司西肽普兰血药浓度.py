import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y1 = [100,100,100,100,100,100,100,100]
y2 = [50,50,50,50,50,50,50,50]
y3 = [50,25,75,38,88,44,94,47]

plt.figure(figsize=(8,5))
plt.plot(x, y1, marker='o', label='每天一颗')
plt.plot(x, y2, marker='o', label='每天半颗')
plt.plot(x, y3, marker='o', label='隔一天吃半颗')

plt.title('不同服药方案下的血药浓度模拟示意图')
plt.xlabel('时间（天）')
plt.ylabel('相对血药浓度')
plt.ylim(0, 120)
plt.legend()
plt.grid(True)
plt.show()
