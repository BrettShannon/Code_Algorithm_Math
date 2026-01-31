# 💡💡💡32.pow（）函数，幂函数，计算x的y次方，x^y

result = pow(2, 3)
print(result)  # 8

result = 2 ** 3
print(result)  # 8
# 两个结果是一样的

# pow()函数还可以有第三个参数，表示取余数
result = pow(2, 3, 3)  # pow(2, 3, 3)的意思是2^3，然后对3取余数。
print(result)  # 2
# 2^3=8，8%3=2
# 2^3=8，8//3=2，取整除
# 2^3=8，8%3=2，取余数
# 2^3=8，8%3=2，取模

# 33. 💡💡💡divmod()函数，同时返回商和余数，返回一个元组，
quotient, remainder = divmod(10, 3) 
        #意思是10除以3的商和余数，分别赋值给quotient和remainder，用逗号分隔，表示同时赋值。
print(quotient, remainder)  # 3 1  

# 34. 💡💡💡filter()函数，过滤函数，过滤掉不符合条件的[‼️元素]，返回一个迭代器。

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # x % 2 == 0，表示x除以2的余数等于0，即x是偶数。
# numbers是可迭代对象，filter()函数会遍历numbers，对每个元素调用lambda函数，如果lambda函数返回True，则保留该元素，否则过滤掉。
# filter()函数，第一个参数是一个函数，第二个参数是一个可迭代对象，
# filter()函数会遍历可迭代对象(numbers)，对每个元素调用函数，如果函数返回True，则保留该元素，否则过滤掉。
print(even_numbers)  # [2, 4, 6, 8, 10]


# 35. 💡💡💡map()函数，映射函数，将函数应用到可迭代对象的每个元素上，返回一个迭代器。

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = list(map(lambda x: x ** 2, numbers))
# x ** 2，表示x的平方，将函数应用到numbers的每个元素上，返回一个迭代器。
# map()函数，第一个参数是一个函数，第二个参数是一个可迭代对象，
# map()函数会遍历可迭代对象(numbers)，对每个元素调用函数，返回一个迭代器。
print(squared_numbers)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 36. 💡💡💡reduce()函数，归约函数，将函数应用到可迭代对象的每个元素上，返回一个值。
from functools import reduce 

# reduce()函数，第一个参数是一个函数，第二个参数是一个可迭代对象，

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = reduce(lambda x, y: x * y, numbers)  # 这行代码的逻辑是，将numbers的每个元素相乘，返回一个值。
# x, y: x * y，表示x乘以y，将函数应用到numbers的每个元素上，返回一个值。
# reduce()函数会遍历可迭代对象(numbers)，对每个元素调用函数，返回一个值。
print(product)  # 3628800
# 1*2*3*4*5*6*7*8*9*10=3628800

# 37.open()函数，打开文件，返回一个文件对象，可以读取文件内容。
# 38.close()函数，关闭文件，释放资源。

file = open('test.txt', 'r')  # 打开文件，以只读模式打开，返回一个文件对象。
                        # open('test.txt', 'r')，表示打开test.txt文件，以只读模式打开。
content = file.read()  # 读取文件内容，返回一个字符串。
print(content)  # Hello, World!
file.close()  # 关闭文件。

# 39.read()函数，读取文件内容，返回一个字符串。
file = open('test.txt', 'r')  # 打开文件，以只读模式打开，返回一个文件对象。
content = file.read()  # 读取文件内容，返回一个【字符串】。‼️注意，read()函数返回的是一个字符串，而不是一个列表。
print(content)  # Hello, World!
file.close()  # 关闭文件。

# 40.write()函数，写入文件内容，返回一个整数，表示写入的字节数。
file = open('test.txt', 'w')  # 打开文件，以写入模式打开，返回一个文件对象。
file.write('Hello, World!')  # 写入文件内容，返回一个整数，表示写入的字节数。
file.close()  # 关闭文件。

# 41.append()函数，追加文件内容，返回一个整数，表示追加的字节数。

file = open('test.txt', 'a')  # 打开文件，以追加模式打开，返回一个文件对象。
file.write('Hello, World!')  # 追加文件内容，返回一个整数，表示追加的字节数。
file.close()  # 关闭文件。

# append（）还可以在列表末尾添加元素。
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # 在列表末尾添加元素，返回None。
print(numbers)  # [1, 2, 3, 4, 5, 6]

# 42. 💡💡💡extend()函数，扩展列表，将一个可迭代对象的元素添加到列表末尾，返回None。
numbers = [1, 2, 3, 4, 5]
more_numbers = [6, 7, 8, 9, 10]
numbers.extend(more_numbers)  # 将more_numbers的元素添加到numbers末尾，返回None。
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # extend()函数，第一个参数是一个可迭代对象，第二个参数是一个列表，
    # extend()函数会遍历可迭代对象，将每个元素添加到列表末尾，返回None。

# 43. 💡💡💡insert()函数，插入元素，在列表的指定位置插入元素，返回None。

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 6)  # 在列表的第2个位置插入元素6，返回None。
print(numbers)  # [1, 2, 6, 3, 4, 5]

# 44. 💡💡💡remove()函数，删除元素，删除列表中第一个匹配的元素，返回None。

numbers = [1, 2, 3, 4, 5]
numbers.remove(2)  # 删除列表中第一个匹配的元素2，返回None。
print(numbers)  # [1, 3, 4, 5]

# 45. 💡💡💡pop()函数，删除元素，删除列表中最后一个元素，返回被删除的元素。

numbers = [1, 2, 3, 4, 5]
last_number = numbers.pop()  # 删除列表中最后一个元素，返回被删除的元素。‼️默认是最后一个元素。
print(last_number)  # 5
print(numbers)  # [1, 2, 3, 4]

# 46. 💡💡💡index()函数，查找元素，返回列表中第一个匹配的元素的索引，如果没有找到，则抛出ValueError异常。

numbers = [1, 2, 3, 4, 5]
index = numbers.index(3)  # 返回列表中第一个匹配的元素的索引，如果没有找到，则抛出ValueError异常。
print(index)  # 2
# index()函数，第一个参数是一个元素，第二个参数是一个列表，
# index()函数会遍历列表，找到第一个匹配的元素，返回其索引，如果没有找到，则抛出ValueError异常。

# 47. 💡💡💡count()函数，统计元素，返回列表中指定元素出现的次数。

numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
count = numbers.count(1)  # 返回列表中指定元素出现的次数。
print(count)  # 2
print(type(count))  # <class 'int'>
# count()函数，第一个参数是一个元素，第二个参数是一个列表，
# count()函数会遍历列表，统计指定元素出现的次数，返回一个整数。

# 48. 💡💡💡sort()函数，排序函数，对列表进行排序，返回None。

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # 对列表进行排序，返回None。
print(numbers)  # [1, 2, 5, 5, 6, 9]
# sort()函数，第一个参数是一个列表，第二个参数是一个函数，
# sort()函数会遍历列表，对每个元素调用函数，返回一个列表。

# 49. 💡💡💡reverse()函数，反转函数，反转列表中的元素，返回None。

numbers = [1, 2, 3, 4, 5]
numbers.reverse()  # 反转列表中的元素，返回None。
print(numbers)  # [5, 4, 3, 2, 1]

