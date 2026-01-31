b_list = ['foo', 'peekaboo', 'baz']
b_list.append('draft') # 使用append（）在列表末尾添加元素'draft'
# # print(b_list)  # 输出 ['draft']

b_list.insert(1, 'red')
# # 使用insert()在列表的指定位置插入元素'red',1的意思是将'red'插入到索引1的位置
# # 也就是在'foo'和'peekaboo'之间
# # 注意：insert()方法不会覆盖原有元素，而是将新元素插入到指定位置
# # 这意味着原有元素会向后移动一个位置

# # print(b_list)  # 输出 ['foo', 'red', 'peekaboo', 'baz']

# x = b_list.pop(2)
# print(x)
# # 使用pop()方法删除列表中索引为2的元素，并返回该元素
# # ⚠️ 注意：pop()方法会修改原列表，并返回被删除的元素
# # print(b_list)  # 输出 ['foo', 'red', 'baz']
# print(b_list)

b_list.append('foo')
print(b_list)

b_list.remove('foo')
# 使用remove()方法删除列表中⚠️第一个⚠️出现的元素'foo'
# 使用remove删除某个值时，remove会先寻找第一个值并删除
print(b_list)

print('draft' in b_list)  # 检查'draft'是否在列表中，输出True或False
print('draft' not in b_list)  # 检查'draft'是否不在列表中，输出True或False

