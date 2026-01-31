'''
aa = set([2, 2, 2, 1, 3, 3])
# ❗️ set()是一个无序不重复元素集 
# 可以用来去除重复元素
# 也可以用来进行集合运算
# 例如：并集、交集、差集等
# 这里的aa将只包含唯一的元素

print(aa)  # 输出: {1, 2, 3}

bb = set({2, 2, 2, 1, 3, 3})
print(bb)  # 输出: {1, 2, 3}
'''

'''集合运算示例

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}

# 计算并集
print(a.union(b))  # 并集 # 输出: {1, 2, 3, 4, 5, 6, 7, 8}
print(a | b)  # 并集 # 输出: {1, 2, 3, 4, 5, 6, 7, 8}

# 计算交集
print(a.intersection(b))  # 交集 # 输出: {3, 4, 5}
print(a & b)  # 交集 # 输出: {3, 4, 5}


c = a.copy()  # 创建a的副本
c |= b  # 将b的元素添加到c中
# |读作“或”，表示并集操作。这将修改c，使其包含a和b的所有元素
print(c)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8}

d = a.copy()  # 创建a的副本
d &= b  # 将d修改为a和b的交集
# &读作“与”，表示交集操作。这将修改d，使其只包含a和b的共同元素
print(d)  # 输出: {3, 4, 5}
'''

'''
my_data = [1, 2, 3, 4]
my_set = {tuple(my_data)}  # 将列表转换为元组，然后放入集合中
print(my_set)  # 输出: {(1, 2, 3, 4)}
# 注意：列表是不可哈希的，不能直接放入集合中，但元组是可哈希的，可以放入集合中
# 这使得集合可以存储不可变的数据类型，如元组，而不能存储可变的数据类型，如列表
# 集合中的元素必须是不可变的（可哈希的），因此列表不能直接存储
'''

'''
a_set = {1, 2, 3, 4, 5}
print({1, 2, 3}.issubset(a_set))  # 检查{1, 2, 3}是否是a_set的子集
# 输出: True
'''

# print({1, 2, 3,} == {3, 2, 1})  # 检查两个集合是否相等
# # 输出: True

'''
# 列表、集合和字典推导式

[expr for val in collection if condition]  # 列表推导式
# 相当于👇

results = []
for val in collection:
    if condition:
        results.append(expr)

{key: value for val in collection if condition}  # 字典推导式
{expr for val in collection if condition}  # 集合推导式
'''

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']

unique_lengths = {len(x) for x in strings} # 集合推导式
print(unique_lengths)  # 输出: {1, 2, 3, 4, 6}

print(set(map(len, strings)))  # 使用map函数和set转换为集合 # 输出: {1, 2, 3, 4, 6} 
# ❗️ map()函数的作用是将len函数应用于strings中的每个元素，然后将结果转换为集合
# 集合推导式和map函数的区别在于，集合推导式更直观易读，而map函数更简洁
# 选择使用哪种方式取决于个人喜好和代码的可读性
# 集合推导式通常更易于理解和维护，尤其是在处理复杂的逻辑时
# map函数在处理简单的转换时更简洁，但可能不如集合推导式直观

loc_mapping = {val: index for index, val in enumerate(strings)} # 字典推导式
# 使用 enumerate 函数创建一个字典，键是字符串，值是它们的索引
print(loc_mapping)  # 输出: {'a': 0, 'as': 1, 'bat': 2, 'car': 3, 'dove': 4, 'python': 5}
# ❗️ enumerate()函数返回一个包含索引和值的迭代器
# 这使得我们可以在遍历字符串列表时同时获取索引和值
# 这种方式在需要同时处理索引和值时非常有用
# 例如，在创建字典时，我们可以使用索引作为键，字符串作为值