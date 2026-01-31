'''
def my_function(x, y, z = 1.5):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)
    
my_function(5, 6, z = 0.7)

# 在上面的函数中，x、y 是必需参数，z 是可选参数，默认值为 1.5。
# x、y是位置参数，而z是关键字参数。
# 当调用 my_function(5, 6, z = 0.7) 时，
# x 被赋值为 5，y 被赋值为 6，z 被赋值为 0.7。
# 因为 z 小于等于 1，所以
# 函数将返回 z 除以 (x + y)，即 0.7 / (5 + 6)，结果为 0.06363636363636363。

# 前面的例子也可以写为：
my_function(x = 5, y = 6, z = 0.7)
# 或者：
my_function(y = 6, x = 5, z = 0.7)

'''

'''命名空间、作用域和局部函数👇'''
# ⚠️ 这一节不太理解，后面有机会继续学习

'''
def func():
    a = []
    for i in range(5):
        a.append(i)

# 上面的代码的作用是创建一个列表 a，并将 0 到 4 的数字添加到列表中。
# 但是这个 a 是局部变量，只在 func 函数内部可见。
# 如果在函数外部尝试访问 a，将会引发 NameError。

a = None

def bind_a_variable():
    global a
    a = []
bind_a_variable()

print(a)  
'''

'''返回多个值'''
'''
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c

a, b, c = f()
'''

'''
import re
# re是 Python 的正则表达式模块，用于字符串的模式匹配和处理。
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California']

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()  # 去除首尾空格
        value = re.sub('[!#?]', '', value) # 去除特定字符
        value = value.title()  # 将首字母大写
        result.append(value) # 将处理后的字符串添加到结果列表
    return result
    print(result)
# 函数clean_strings()的作用是对传入的字符串列表进行处理，
# 去除首尾空格，去除特定字符（!、#、?），
# 并将每个字符串的首字母大写，最后返回处理后的列表。

clean_strings(states) # 调用函数并传入states列表。
'''
import re

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California']

def remove_punctuation(value):
    return re.sub('[!#?]', '', value)  # 去除特定字符

clean_ops = [str.strip, remove_punctuation, str.title]
# 定义一个操作函数列表，包含三个函数：
# 1. str.strip：去除字符串首尾空格。
# 2. remove_punctuation：去除特定字符（!、#、?）。
# 3. str.title：将字符串的首字母大写。

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
#     print(result)
# 函数clean_strings()的作用是对传入的字符串列表进行处理，
# 使用传入的操作函数列表ops对每个字符串进行处理，
# 最后返回处理后的列表。

clean_strings(states, clean_ops)  # 调用函数并传入states列表和操作函数列表。
print(clean_strings(states, clean_ops))

# 还可以将函数用作其他函数的函数，比如内置的map()函数。
# map()函数可以将一个函数应用于一个可迭代对象的每个元素。

for x in map(remove_punctuation, states):
    print(x)