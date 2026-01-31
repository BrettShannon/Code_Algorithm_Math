l = [1, 2, 3, 4]

print(type(l))
print()

print(l[0])
print()

print(l + l)
print()

print(l * 2)
print()

print(sum(l))  #
print()

print(l.__sizeof__()) # __sizeof__() 功能是查看对象占用的内存大小
print()

# 以下是书上没有的：

print(l.__len__()) # __len__() 功能是查看对象的长度
print()

print(l.__getitem__(0)) # __getitem__() 功能是获取对象的某个元素
print()

print(l.__setitem__(0, 5)) # __setitem__() 功能是设置对象的某个元素
print()

print(l.__delitem__(0)) # __delitem__() 功能是删除对象的某个元素
print()

print(l.__contains__(1)) # __contains__() 功能是判断对象是否包含某个元素
print()

print(l.__iter__()) # __iter__() 功能是返回对象的迭代器
print()

print(l.__reversed__()) # __reversed__() 功能是返回对象的逆序迭代器
print()

print(l.__str__()) # __str__() 功能是返回对象的字符串表示
print()

print(l.__repr__()) # __repr__() 功能是返回对象的字符串表示

# ……