print(int(True))  # 1
print(int(False))  # 0
print(int(True) + int(False))  # 2
print(True +1)  # 2
print()

# 例：计算列表里共有多少偶数:
# 一般来说，需要写一个循环+分支结构，如下：
numbers = [1, 2, 4, 5, 7]
count = 0

for i in numbers: # 遍历列表中的每个元素
    if i % 2 == 0: # 判断是否为偶数
        count += 1 # 偶数计数加1

print(count)  # 2

# 利用“布尔值作为整型使用”的特性，只需要一个简单的表达式,如下：
count = sum(i % 2 == 0 for i in numbers)
                    # 💡 此处的表达式i % 2 == 0会返回布尔值True或False，该结果会被当作1或0由sum函数累加求和。
print(count)  # 2


"""
千问：
我们来逐行详细讲解这段 Python 代码：
python

numbers = [1, 2, 4, 5, 7]
count = 0
count = sum(i % 2 == 0 for i in numbers)
print(count)  # 2

第 1 行：定义列表
python


numbers = [1, 2, 4, 5, 7]
创建一个包含 5 个整数的列表：[1, 2, 4, 5, 7]。
第 2 行：初始化变量（其实没用上）
python

编辑



count = 0
这行代码将 count 初始化为 0。
但注意：下一行立刻重新赋值给 count，所以这行其实是多余的，可以删掉。
第 3 行：核心逻辑 —— 计算偶数个数
python

编辑



count = sum(i % 2 == 0 for i in numbers)
我们拆解来看：
🔹 1. i % 2 == 0 是什么？
% 是取模运算符（求余数）。
i % 2 == 0 判断 i 是否能被 2 整除：
如果 i 是偶数 → 余数为 0 → 表达式为 True
如果 i 是奇数 → 余数为 1 → 表达式为 False
对 numbers 中每个元素计算：
表格
i	i % 2 == 0
1	False
2	True
4	True
5	False
7	False
所以这个表达式生成一个布尔值序列：[False, True, True, False, False]
🔹 2. (i % 2 == 0 for i in numbers) 是什么？
这是一个 生成器表达式（generator expression），不是列表。
它会逐个产生上述的 True/False 值，但不一次性存入内存（高效）。
🔹 3. sum(...) 为什么能加布尔值？
在 Python 中，bool 是 int 的子类：
True 的数值是 1
False 的数值是 0
所以 sum([False, True, True, False, False]) 等价于：
python

编辑



sum([0, 1, 1, 0, 0])  # 结果是 2
✅ 因此，sum(i % 2 == 0 for i in numbers) 实际上就是统计满足条件（是偶数）的元素个数。
第 4 行：输出结果
python

编辑



print(count)  # 2
列表 [1, 2, 4, 5, 7] 中有 2 个偶数（2 和 4），所以输出 2。

✅ 更清晰的等价写法（便于理解）
如果你刚学 Python，也可以写成显式的循环：
python

numbers = [1, 2, 4, 5, 7]
count = 0
for i in numbers:
    if i % 2 == 0:
        count += 1
print(count)  # 2
这段代码和原代码功能完全相同，都是计算偶数的个数。

而原代码用 sum + 生成器 是一种更 Pythonic（简洁、高效）的写法。

💡 小结
sum(condition for item in iterable) 是 Python 中统计满足条件元素个数的经典技巧。
利用了 True == 1、False == 0 的特性。
适用于各种计数场景，例如：
python


# 统计正数个数
sum(x > 0 for x in [-1, 0, 2, 3])

# 统计长度大于3的单词个数
sum(len(word) > 3 for word in ['a', 'hello', 'hi', 'world'])
希望这个讲解清楚啦！如果还有疑问，欢迎继续问 😊
"""