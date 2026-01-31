# # enumerate() 函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标
# # 举例：
# seq = [7, 2, 3, 7, 5, 6, 0, 1]
# for i, element in enumerate(seq):
#     print(i, element)

# some_list = ['foo', 'bar', 'baz']
# mapping = {}

# for i, v in enumerate(some_list):
#     mapping[v] = i  # 将元素作为键，索引作为值存入字典
# print(mapping)  # 输出 {'foo': 0, 'bar': 1, 'baz': 2}

# --------------

# k = sorted([7, 2, 3, 7, 5, 6, 0, 1])
# # sorted() 函数用于对可迭代对象进行排序，返回一个新的列表
# print(k)  # 输出排序后的列表
# kk = sorted('horse race')
# print(kk)  # 输出排序后的字符串列表

# --------------
# seq_1 = ['foo', 'bar', 'baz']
# seq_2 = ['one', 'two', 'three']
# zipped = zip(seq_1, seq_2)
# # zip() 函数用于将多个可迭代对象打包成一个元组，返回一个迭代器
# print(list(zipped))  # 输出 [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]
# seq_3 = ['False', 'True',]
# xy = list(zip(seq_1, seq_2, seq_3))
# print(xy)  # 输出 [('foo', 'one', 'False'), ('bar', 'two', 'True'), ('baz', 'three', None)]
# # zip() 函数在迭代对象长度不一致时，返回的元组长度以最短的可迭代对象为准

# #--------
# for i, (a, b) in enumerate(zip(seq_1, seq_2)):
#     print(i, a, b)  # 输出索引和对应的元素
# # zip() 函数可以用于并行迭代多个序列

# --------------

# pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Sandy', 'Koufax')]
# # pitchers的意思是投手列表，每个投手由名字和姓氏组成的元组表示
# # ⚠️ zip() 函数可以用于将多个序列打包成一个元组列表
# # 例如，将投手的名字和姓氏分开存储
# # 通过解包操作将元组列表转换为两个独立的列表
# first_names, last_names = zip(*pitchers)
# print(first_names)  # 输出 ('Nolan', 'Roger', 'Sandy')
# print(last_names)   # 输出 ('Ryan', 'Clemens', 'Koufax

#---------
x = list(reversed(range(10)))
# reversed() 函数用于反转一个序列，返回一个迭代器
# range(10) 生成一个从 0 到 9 的整数序列
# ⚠️ list() 将迭代器转换为列表
# 结果是一个从 9 到 0 的整数列表
print(x)  # 输出 [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
