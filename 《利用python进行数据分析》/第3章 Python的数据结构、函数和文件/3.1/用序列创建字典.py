# mapping = {}
# for key, value in zip(key_list, value_list):
#     mapping[key] = value

# mapping = dict(zip(range(5), reversed(range(5))))
# 创建一个字典，将键映射到值
# 这里使用了 range(5) 生成键 [0, 1, 2, 3, 4]，并使用 reversed(range(5)) 生成值

# print(mapping)  # 输出 {0: 4, 1: 3, 2: 2, 3: 1, 4: 0}

# ----------
# if key in some_dict:
#     value = some_dict[key]
# else:
#     value = default_value

# value = some_dict.get(key, default_value)
# 使用字典的 get 方法来获取键对应的值，如果键不存在则返回默认值
# .get() 方法的作用是提供一个更简洁的方式来处理键不存在的情况

''' 
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
# 创建一个字典，将字母映射到单词列表
for word in words:
    letter = word[0] # letter的作用是获取单词的首字母
    if letter not in by_letter:
        by_letter[letter] = [word] # 如果字母不在字典中，则添加一个新条目
    else:
        by_letter[letter].append(word) # 如果字母已存在，则将单词添加到对应的列表中
        
# 使用字典的 get 方法来简化代码
print(by_letter)  # 输出 {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}
'''

'''
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}

for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
# 使用 setdefault 方法来简化代码
# setdefault 方法会检查字典中是否存在指定的键，如果不存在则添加该键并设置一个默认值
# 如果键已存在，则返回该键对应的值
# 这里的默认值是一个空列表，并将单词添加到该列表中
print(by_letter)  # 输出 {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}
'''

'''
from collections import defaultdict # 使用 defaultdict 来简化字典的创建和操作
# collections 模块提供了许多有用的容器数据类型，其中 defaultdict 是一个非常有用的类
# 它允许你为字典的键提供一个默认值，这样在访问不存在的键时不会抛出 KeyError 异常

words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = defaultdict(list) 
# 使用 defaultdict 来创建一个字典，将字母映射到单词列表
# list 是一个内置的 Python 数据类型，用于存储有序的元素集合
# defaultdict(list) 创建了一个字典，其中每个键的默认值是一个空列表
# 这样，当我们访问一个不存在的键时，它会自动创建一个空列表
# defaultdict(list) 的作用是简化字典的创建和操作
# 遍历单词列表，将每个单词的首字母作为键，将单词添加到对应的字母列表中
# 这样可以更方便地将单词按首字母分组

for word in words:
    letter = word[0]
    by_letter[letter].append(word) # 将单词添加到对应的字母列表中
# 使用 defaultdict 来简化代码
# defaultdict 是 collections 模块中的一个类，它允许你为字典的键提供一个默认值
# 默认值，这样在访问不存在的键时不会抛出 KeyError 异常
# 在这里，我们使用 defaultdict(list) 来创建一个字典，其中每个键的默认值是一个空列表
# 当我们访问一个不存在的键时，它会自动创建一个空列表
print(by_letter)  # 输出 {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}
'''

'''
# 有效的健类型

print(hash('string'))  # 字符串类型的键
# hash()的作用是计算对象的哈希值
print(hash((1, 2, (2, 3))))  # 元组类型的键
# print(hash((1, 2, [2, 3])))  # ⚠️ 列表类型的键会抛出 TypeError，因为列表是不可哈希的
'''

'''
a = (1, 2, 3)  # 一个元组对象
print(hash(a))  # 输出固定的哈希值
# 这个元组 a 在其生命周期内没有被修改（其实元组本身也无法修改），所以它的哈希值是稳定的。
# 如果你试图把一个可变对象（如列表）放入集合，会报错，因为它的内容可能在生命周期中被更改。
'''

'''
“可哈希的对象一般都是固定不变的”——也就是说，这类对象的内容在其生命周期内不会发生改变，因此它们的哈希值才是稳定且固定的。

举例来说：

**整数、浮点数、字符串、元组（且元组内元素也不可变）**都是不可变对象，因此它们是可哈希的。
列表、字典、集合等是可变对象，因为它们的内容可以修改，所以它们通常是不可哈希的。
这种“固定不变”保证了哈希值的稳定性，进而保证了哈希表（如字典、集合）中键的唯一性和查找效率。

这里的“生命周期”是指一个对象从被创建（初始化）到被销毁（被垃圾回收或失去所有引用）的整个时间段。
在这段时间内，如果一个对象是“可哈希的”，它的内容应保持不变，这样才能保证其哈希值始终一致。
否则，如果对象内容改变，其哈希值也会改变，就会破坏哈希结构（如set、dict）的正常工作。

'''
'''
print(hash(42))
print(hash(3.14))
print(hash('hello'))
print(hash(10000))
'''

d = {}
d[tuple([1, 2, 3])] = 5 # tuple()将列表转换为元组作为键
# 👆意思是：键 = 值

print(d)  # 输出 {(1, 2, 3): 5}
# ⚠️ 这里使用了 tuple() 函数将列表转换为元组，因为元组是不可变的，可以作为字典的键
# ⚠️ 而列表是可变的，不能作为字典的键

# 这段代码创建了一个字典 d，并将一个元组 (1, 2, 3) 作为键，5 作为值
# 最终输出的字典 d 包含一个键值对 {(1, 2, 3): 5}
# 这说明元组 (1, 2, 3) 是一个有效的字典键，因为它是不可变的
# 而列表 [1, 2, 3] 是可变的，不能直接作为字典键
# 通过将列表转换为元组，我们可以使用它作为字典的键

