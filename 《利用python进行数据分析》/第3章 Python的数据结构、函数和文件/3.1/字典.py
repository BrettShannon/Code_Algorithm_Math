empty_dict = {}
d_1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
print(empty_dict)  # 输出空字典 {}
print(d_1)  # 输出 {'a': 'some value', 'b': [1, 2, 3, 4]}

d_1[7] = 'an integer'
print(d_1)  # 输出 {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}

print(d_1['b'])  # 输出 [1, 2, 3, 4]
print('b' in d_1)  # 检查键 'b' 是否在字典中，输出 True

d_1[5] = 'some value'
print(d_1)  # 输出 {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer', 5: 'some value'}

d_1['dummy'] = 'another value' # 添加一个新的键值对
print(d_1)  # 输出 {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer', 5: 'some value', 'dummy': 'another value'}

del d_1[5]  # 删除键为 5 的键值对
print(d_1)  # 输出 {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer', 'dummy': 'another value'}

ret = d_1.pop('dummy')  # 删除键 'dummy' 并返回其值
print(ret)  # 输出 'another value'


print(list(d_1.keys()))  # 输出字典的所有键 ['a', 'b', 7]

print(list(d_1.values()))  # 输出字典的所有值 ['some value', [1, 2, 3, 4], 'an integer']

d_1.update({'b': 'foo', 'c': 12})  # 更新字典，修改键 'b' 的值并添加新键 'c'
print(d_1)  # 输出 {'a': 'some value', 'b': 'foo', 7: 'an integer', 'c': 12}
