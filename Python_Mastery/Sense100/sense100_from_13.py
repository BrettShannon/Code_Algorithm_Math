# 13 将列表a拆分成奇数组和偶数组两个列表：
'''

a = [0,1,2,3,4,5,6,7,8,9]
b = a[::2] # 意思是删除列表a中索引为偶数的元素,‼️[::2]表示从0开始，每隔2个元素取一个。
                # ‼️::表示从头到尾
c = a[1::2] # 意思是删除列表a中索引为奇数的元素,‼️[1::2]表示从1开始，每隔2个元素取一个
print(b)
print()
print(c)
print()

# 14 分别根据列表a中每个子列表的第一个元素和最后一个元素大小进行排序
a = [[6, 5], [3, 7], [2, 8]]
print(sorted(a, key=lambda x: x[0])) # 意思是按照列表a中每个子列表的第一个元素进行排序,
            # ‼️key=lambda x: x[0]表示按照列表a中每个子列表的第一个元素进行排序
print()

a = [[6, 5], [3, 7], [2, 8]]
print(sorted(a, key=lambda x: x[-1])) # 意思是按照列表a中每个子列表的最后一个元素进行排序
print()

# 15
a = [1,4,7,2,5,8]
a[3:3] = ['x', 'y', 'z'] # 在列表a中索引为3的位置插入['x', 'y', 'z']
                # ‼️ 如果写成[3:4],索引为3的元素2会被替换成['x', 'y', 'z']
print(a)
print()
'''

'''
# 16 快速生成由[5,50)区间内的整数组成的列表
print(list(range(5, 50))) # ‼️ range(5,50)表示从5开始到50结束，但不包括50
print()
'''

# 17
a = [1, 2, 3]
b = a
print(id(a) == id(b)) # ‼️ 对象a和对象b在内存中是同一个，所以会出现关联
print()
b = a.copy() # ‼️ 正确的做法是复制一个新的对象——使用copy()方法创建一个新的对象b
print(id(a) == id(b)) # 对象a和对象b在内存中不是同一个，所以不会出现关联
print()

# 18 zip()函数
print([(a,b) for a, b in zip(['x', 'y', 'z'], [1, 2, 3])])
                    # ‼️ zip()函数将两个列表中的元素一一配对，形成元组
# ‼️ 列表推导式用于生成包含这些元组的列表
print()

# 👇vscode 给的例子：
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
print(list(zip(a, b, c))) # ‼️ zip()函数将三个列表中的元素一一配对，形成元组
print()

# 19 .key()
d = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
print([key for key in d.keys()]) # ‼️ 列表推导式用于生成包含字典d中所有键的列表
                                 # d.key() 返回的类型是 dict_keys, 不是列表类型
print(type(d.keys()))
print()

# 20 .values()
d = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
print([key  for key in d.values()]) # ‼️ 列表推导式用于生成包含字典d中所有值的列表
                                    # d.values() 返回的类型是 dict_values, 不是列表类型,dict_values是一种视图类型
print(type(d.values()))
print()
