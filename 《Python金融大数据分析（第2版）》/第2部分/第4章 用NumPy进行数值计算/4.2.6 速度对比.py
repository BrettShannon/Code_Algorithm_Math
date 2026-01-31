import random # 随机数
import time # 时间
'''
I = 5000 # 迭代次数
# I 的意思是：迭代次数，也就是生成5000*5000的二维列表

%time mat = [[random.gauss(0, 1) for j in range(I)] \
             for i in range(I) ]
# %time 只能在 IPython/Jupyter 环境使用。

# 上面这段代码的意思是：生成一个5000*5000的二维列表，每个元素都是随机数
# random.gauss(0, 1) 生成均值为0，标准差为1的正态分布随机数
'''


I = 5000

start = time.time() # 记录开始时间
# time.time() 返回当前时间的时间戳
mat = [[random.gauss(0, 1) for j in range(I)] \
       for i in range(I)]
end = time.time()


# print(f"Time elapsed: {end - start} seconds") # 打印时间差


print(mat[0][:5]) # 打印第一行前5个元素
# mat 的意思是：二维列表

start = time.time() # 记录开始时间
sum = ([sum(l) for l in mat]) # 计算每一行的和
end = time.time() # 记录结束时间

# print(f"Time elapsed: {end - start} seconds") # 打印时间差

import sys # 系统

print(sum([sys.getsizeof(l) for l in mat])) # 计算每一行的字节数
# sys.getsizeof() 返回对象的大小（以字节为单位）

