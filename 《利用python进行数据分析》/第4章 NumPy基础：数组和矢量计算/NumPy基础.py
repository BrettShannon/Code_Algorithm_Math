import numpy as np

my_arr = np.arange(1000000)
print(my_arr)
'''
特点：

内存连续存储，计算速度快。

支持 向量化操作（如对整个数组进行数学运算）。
'''

my_list = list(range(1000000))
print(my_list)
'''
特点：

列表是 动态数组，存储灵活但计算效率低于 NumPy 数组。
'''

'''
NumPy 数组 vs Python 列表
特性	    NumPy 数组 (np.arange)	**        Python 列表 (list(range)) **
内存占用	 更小（连续存储）                	更大（存储对象指针）
计算速度	 快（C 语言优化）	                慢（Python 解释执行）
功能	    支持向量化运算（如 arr * 2）	    只能循环操作
打印行为	 自动省略中间部分	                可能完整打印（导致卡顿）
适用场景	 数值计算、机器学习	                通用编程、动态数据
'''

'''
为什么用 NumPy？
高效计算：NumPy 数组比 Python 列表快 10-100 倍（尤其是大数据场景）。

便捷操作：支持矩阵运算、广播机制等科学计算功能。

内存优化：存储相同数据时，NumPy 占用的内存更少。
'''