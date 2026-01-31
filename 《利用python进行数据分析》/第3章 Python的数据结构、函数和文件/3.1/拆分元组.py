# tup = (1, 2, 3, 4, 5)
# a, b, c, d, e = tup
# # 拆分元组中的元素
# print(a)  # 输出1
# print(b)  # 输出2
# print(c)  # 输出3
# print(d)  # 输出4
# print(e)  # 输出5

# tup = 4, 5, (6, 7)
# a, b, (c, d) = tup
# # 拆分元组中的元素
# print(a)  # 输出4
# print(b)  # 输出5
# print(c)  # 输出6
# print(d)  # 输出7

# values = 1, 2, 3, 4, 5
# a, b, *rest = values # 拆分元组中的元素，rest会包含剩余的元素
# print(a, b)      # 输出1 2
# print(rest)  # 输出剩余的元素 [3, 4, 5]

# .count() 方法用于计算元组中某个元素的出现次数
a = (1, 2, 2, 2, 3, 4, 2)
print(a.count(2))  # 计算元组中元素2的出现次数
