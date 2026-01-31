import bisect
# bisect是一个用于维护已排序列表的模块
# 它主要用于对有序列表进行二分查找和插入操作。

c = [1, 2, 2, 2, 3, 4, 7]
print(bisect.bisect(c, 2))
# bisect.bisect()函数 返回值是数字2在列表c中应该插入的位置，插入后仍保持列表有序。
# 在c中，2出现了3次，索引分别是1、2、3，插入点就是索引4。所以这行代码输出：4

print(bisect.bisect(c, 5))
# bisect.bisect()函数返回5在列表c中的插入位置，插入后仍保持列表有序。

print(bisect.insort(c, 6))
# bisect.insort()函数在列表c中插入6，并保持列表的有序性。
print(c)
