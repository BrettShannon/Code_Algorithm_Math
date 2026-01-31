import numpy as np

a = np.array([[1, 2, 3]]) # 注意，这里a的元素是1行3列的数组，所以a是一个1行3列的数组

b =np.array([[1], [2], [3]]) # 注意，这里b的元素是1行1列的数组，所以b是一个3行1列的数组

print(a)
print()

print(a.shape) # 输出(1, 3)，表示a是一个1行3列的数组
print()

print(b)
print()

print(b.shape) # 输出(3, 1)，表示b是一个3行1列的数组