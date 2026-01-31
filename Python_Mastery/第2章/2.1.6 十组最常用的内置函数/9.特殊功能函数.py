# 9.特殊功能函数enumerate（ ），zip（ ），map（ ），chr（ ），ord（ ）

for index, item in enumerate([True, False, None]):
    print(index, item, sep='->') # ‼️sep意思是分隔符，默认是空格
    # 输出：0->True 1->False 2->None

# ✅ 总结一句话：
# 这段代码的意思是：
# 用 enumerate() 同时遍历列表 [True, False, None] 的索引和值，并用箭头符号“->”连接打印出来。

'''
一、enumerate() 的作用
enumerate() 是 Python 的一个内置函数，‼️用来在遍历可迭代对象（如列表、元组等）时，同时获取元素的【索引】和【值】。

语法：
enumerate(iterable, start=0)
iterable：要遍历的可迭代对象；
start：索引从哪个数字开始，默认是 0。

二、循环的含义
enumerate([True, False, None]) 会生成一个带索引的可迭代对象：

index	item
0	True
1	False
2	None

三、print(index, item, sep='->')
print() 默认用空格分隔参数，但这里指定了 sep='->'，表示打印时用“->”代替空格。
'''

print()
# ✅ 例子2：
for index, item in enumerate('xyz'):
    print(index, item, sep='->') # 输出：0->x 1->y 2->z


print()

# 🧀️🧀️🧀️ zip() 函数, 将两个列表合并成一个元组列表
a = ['x', 'y', 'z']
b = [1, 2, 3]
for k, v in zip(a, b):
    print(k, v, sep='->') # 输出：x->1 y->2 z->3
# ✅ 总结一句话：
# 这段代码的意思是：
# 用 zip() 将两个列表合并成一个元组列表，然后用 for 循环遍历这个元组列表，并用箭头符号“->”连接打印出来。
#
# ✅ 注意：
# ‼️ zip() 函数会按照最短的那个列表的长度，生成元组列表。
# 如果两个列表的长度不同，那么生成的元组列表的长度，‼️ 会等于最短的那个列表的长度。
# 例如，如果 a 的长度是 3，b 的长度是 2，那么生成的元组列表的长度就是 2。

# 🧀️🧀️🧀️ map() 函数，将一个函数应用到可迭代对象的每一个元素上,并返回一个可迭代对象,
# 这个可迭代对象中的元素是函数的返回值,而不是函数本身。

def extract(x): # 开3次方
    return pow(x, 1/3) # 开3次方,
        # ‼️ pow()函数是Python的内置函数，用来计算一个数的n次方,pow(x, 1/3)就是计算x的1/3次方，也就是x的开3次方。

result = map(extract, [7, 8, 9]) # 将extract函数应用到列表[7, 8, 9]的每一个元素上，并返回一个可迭代对象result.
print(list(result)) # 将迭代对象转为list
    # 输出：[1.912931182772389, 2.0, 2.089935061535337]

# 💡💡💡 以下是另一种写法，使用lambda表达式：
print(list(map(lambda x:pow(x, 1/3), [7, 8, 9])))   # 输出：[1.912931182772389, 2.0, 2.089935061535337]

# ✅ 总结一句话：
# 这段代码的意思是：
# 用 map() 函数将 extract 函数应用到列表 [7, 8, 9] 的每一个元素上，并返回一个可迭代对象 result。
# 然后用 list() 函数将 result 转为列表，并打印出来。

# 💡💡💡 另一种写法，使用 lambda 表达式：
# 用 map() 函数将 lambda 表达式应用到列表 [7, 8, 9] 的每一个元素上，并返回一个可迭代对象 result。
# 然后用 list() 函数将 result 转为列表，并打印出来。

# ✅ 注意：
# ‼️ map() 函数会按照最短的那个可迭代对象的长度，生成可迭代对象。
# 如果两个可迭代对象的长度不同，那么生成的可迭代对象的长度，‼️ 会等于最短的那个可迭代对象的长度。
# 例如，如果 a 的长度是 3，b 的长度是 2，那么生成的可迭代对象的长度就是 2。

# 🧀️🧀️🧀️ chr() 函数，将一个整数转换为对应的 Unicode 字符
print(chr(65)) # 输出：A
print()

print(ord('A')) # 输出：65, ord()函数是Python的内置函数，用来获取一个字符的Unicode编码。
print(ord('Z')) # 输出：90
print()

for i in range(26):
    print(chr(65+i), sep='', end='') # 输出：ABCDEFGHIJKLMNOPQRSTUVWXYZ

# ✅ 总结一句话：
# 这段代码的意思是：
# 用 chr() 函数将 65 到 90 的整数转换为对应的 Unicode 字符，并打印出来。
# 然后用 ord() 函数将 'A' 和 'Z' 转换为对应的 Unicode 编码，并打印出来。
# 最后用 for 循环遍历 26 个字母，并用 chr() 函数将 65 到 90 的整数转换为对应的 Unicode 字符，并打印出来。


