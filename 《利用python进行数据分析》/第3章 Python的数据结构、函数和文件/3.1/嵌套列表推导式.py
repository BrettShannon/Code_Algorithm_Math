'''
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
# 使用列表推导式来筛选出包含两个或更多字母'e'的名字
# 这里的列表推导式会遍历all_data中的每个子列表，并
# 对每个名字进行检查，如果名字中包含两个或更多的'e'，则
# 将其添加到name_of_interest列表中

# 用for循环和列表推导式来实现：
name_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') >= 2] # 列表推导式
    name_of_interest.extend(enough_es) # 将符合条件的名字添加到name_of_interest列表中
print(name_of_interest)  # 输出: ['Steven']

# 用嵌套列表推导式来实现：
result = [name for names in all_data for name in names if name.count('e') >= 2]
print(result)  # 输出: ['Steven']
'''

some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

flattened = [x for tup in some_tuples for x in tup] # 将嵌套元组展平为单一列表
print(flattened)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 这里的列表推导式会遍历some_tuples中的每个元组
# 并将每个元组中的元素添加到flattened列表中
# 结果是一个包含所有元组元素的单一列表
# 这是一种常见的用法，可以将嵌套结构展平
# 例如，将嵌套列表或元组展平为单一列表
# 这种方法可以用于处理多维数据结构，使其更易于处理和分析


# ⚠️ 注意：for表达式的顺序与嵌套for循环的顺序相同：
flattened = []
for tup in some_tuples:
    for x in tup:
        flattened.append(x)  # 将每个元组中的元素添加到flattened列表中
print(flattened)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 这种方法与列表推导式的效果相同，但使用了显式的for循环
# 列表推导式是一种更简洁的写法，可以在一行中完成相同的操作
# 但有时使用显式的for循环可以提高代码的可读性，尤其是对于复杂的逻辑或多层嵌套


# 将每个元组转换为列表:
# 使用“分辨列表推导式”的语法
xyz = [[x for x in tup] for tup in some_tuples]  # 将每个元组转换为列表
print(xyz)  # 输出: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 这里的列表推导式会遍历some_tuples中的每个元组
# 并将每个元组转换为列表
# 结果是一个包含多个列表的列表，每个列表对应于原始元组中的元素
# 这种方法可以用于将嵌套元组转换为嵌套列表


# 👆也可以使用显式的for循环来实现相同的操作：
xyz = []
for tup in some_tuples:
    xyz.append([x for x in tup])  # 将每个元组转换为列表并添加到xyz中
print(xyz)  # 输出: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 这种方法与列表推导式的效果相同，但使用了显式的for循环
# 列表推导式是一种更简洁的写法，可以在一行中完成相同的操作
# 但有时使用显式的for循环可以提高代码的可读性，尤其是对于复杂的逻辑或多层嵌套