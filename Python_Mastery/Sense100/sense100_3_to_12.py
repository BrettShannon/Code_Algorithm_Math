# 1 将元组（1,2,3）和集合{4,5,6}合并为列表后合并输出
print(list((1,2,3)) + list({4,5,6}))
print(type(list((1,2,3)) + list({4,5,6})))  # 输出合并后数据的类型: list
print()

# 2
a = [1,2,3,4,5,6]
a.insert(0, 7) # 在索引0的位置插入7
print(a)
a.insert(3, 8) # 
print(a)
a.append(0) # 在列表的末尾添加0
print(a)
print()

# 3 翻转列表。.reverse(),[::-1]
a = [1,2,3,4,5,6,7]
a.reverse()  # 翻转列表a
print(a)  # 输出翻转后的列表
b = [7,6,5,4,3,2,1,0]
print(b[::-1])  # 翻转列表b,[::-1] 表示从后往前取元素
print()

# 4
a = [1,2,3,4,5,6,7,8,9,10]
a1 = a[::-1]  # 倒序输出列表a
print(a1)
print(a1.index(5))  # 意思是找到5在列表a1中的索引位置并输出

# index()函数用于查找列表中某个元素的索引位置，如果元素在列表中不存在，则会抛出ValueError异常。
# index()函数的语法是list.index(element, start, end)，
    # 其中element表示要查找的元素，start表示查找的起始位置，end表示查找的结束位置。
    # start和 end参数是可选的，如果不指定，则默认从列表的开头查找到列表的结尾。
# index()函数会返回元素在列表中第一次出现的索引位置。
print()

# 5
a = [True, False, 0, 1, 2, 6, 77, 788]
print(a)
print(a.count(True))  # 意思是统计True的个数
print(a.count(False))  # 意思是统计False的个数
print(a.count(0))  # 意思是统计0的个数
print(a.count(1))  # 意思是统计1的个数
print(a.count(2))  # 意思是统计2的个数
print(a.count(6))  # 意思是统计6的个数
print(a.count(77))  # 意思是统计77的个数
print(a.count(788))  # 意思是统计788的个数
# ‼️count()不区分大小写，所以True和true是相同的，False和false是相同的，0和False是相同的，1和True是相同的。

print()

# 6
a = [True, 1, 0, 'x', None , 'x', False, 2,True]
for i in range(a.count('x')): # 意思是循环a列表中'x'的个数次
    a.remove('x')           # 意思是删除列表a中的所有'x'元素
print(a)  # 输出删除后的列表a
# remove()函数用于删除列表中的某个元素，如果元素在列表中不存在，则会抛出ValueError异常。
# remove()函数的语法是list.remove(element)，其中element表示要删除的元素。
# remove()函数会删除列表中第一个出现的element元素，如果列表中有多个相同的element元素，则只会删除第一个。
print()


# 千问：
# 更好的写法（避免无用变量）：
# 如果循环变量不会被使用，Python 社区通常用 下划线 _ 表示“忽略这个变量”：
# for _ in range(a.count('x')):
#     a.remove('x')
# 这样写更清晰，表明：“我只需要循环 N 次，不关心当前是第几次”。

# 7


# 8
a = list(range(10))
print(a) 
del a[::2] # 意思是删除列表a中索引为偶数的元素,‼️[::2]表示从0开始，每隔2个元素取一个
print(a)  # 意思是输出列表a，列表a的元素是1,3,5,7,9

b = list(range(10))
print(b)
del b[1::2] # 意思是删除列表b中索引为奇数的元素,‼️[1::2]表示从1开始，每隔2个元素取一个
print(b)  # 意思是输出列表b，列表b的元素是0,2,4,6,8

# del()函数可以删除列表中的元素，也可以删除列表中的切片，切片是指列表中的一部分元素。
# 切片的语法是[start:end:step]，start表示切片的起始位置，end表示切片的结束位置，step表示切片的步长。
# 如果不指定start，则默认为0，如果不指定end，则默认为列表的长度，如果不指定step，则默认为1。
# 切片可以用于删除列表中的元素，也可以用于获取列表中的元素。

# 11

print([1 if item>5 else 0 for item in [3, 0, 8, 5, 7]]) 
# 意思是输出列表[1 if item>5 else 0 for item in [3, 0, 8, 5, 7]]，列表中的元素是1,0,1,0,1
# 这个列表的元素是通过列表推导式生成的，列表推导式的语法是:
# ‼️ [expression for item in iterable]，
# 其中expression表示要生成的元素的值，item表示iterable中的元素，iterable表示要遍历的列表。

# 在这个列表推导式中，expression是1 if item>5 else 0，表示如果item大于5，则生成1，否则生成0。
# iterable是[3, 0, 8, 5, 7]，表示要遍历的列表。
# 所以这个列表推导式的意思是，遍历列表[3, 0, 8, 5, 7]，如果元素大于5，则生成1，否则生成0，最后生成一个新的列表[1, 0, 1, 0, 1]。
# 这个列表推导式可以用于生成新的列表，也可以用于修改列表中的元素。

# 12
for index, value in enumerate(['x', 'y', 'z']):
    print('index={}, value={}.format(index, value))')

# 意思是输出列表['x', 'y', 'z']中每个元素的索引和值，索引从0开始，值是元素的值。
# enumerate()函数可以返回一个枚举对象，枚举对象是一个可迭代对象，可以用于遍历列表。
# enumerate()函数的语法是enumerate(iterable)，其中iterable表示要遍历的列表。
# enumerate()函数会返回一个枚举对象，枚举对象是一个可迭代对象，可以用于遍历列表。
# ‼️ 枚举对象中的每个元素都是一个元组，元组的第一个元素是索引，第二个元素是值。
# 所以在这个循环中，index是索引，value是值，index和value的值是enumerate()函数返回的枚举对象中的元素的值。
# 这个循环会输出列表['x', 'y', 'z']中每个元素的索引和值，索引从0开始，值是元素的值。
# enumerate()函数可以用于遍历列表，也可以用于获取列表中每个元素的索引和值。

