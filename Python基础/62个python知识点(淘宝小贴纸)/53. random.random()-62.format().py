
# 50. 💡💡💡random.random()函数，随机函数，生成一个随机数，返回一个浮点数。

import random

number = random.random()  # 生成一个随机数，返回一个浮点数。
print(number)  # 0.12345678901234567
# random.random()函数，没有参数，返回一个0到1之间的随机浮点数。

# 51. 💡💡💡time.sleep()函数，暂停函数，暂停程序执行一段时间，返回None。

import time

time.sleep(5)  # 暂停程序执行5秒，返回None。
print('Hello, World!')  # 5秒后输出Hello, World!
# time.sleep()函数，第一个参数是一个整数，表示暂停的时间，单位是秒，返回None。
# time.sleep(5)表示暂停程序执行5秒。
# time.sleep()函数，可以用来模拟网络延迟，或者暂停程序执行一段时间。

# 52.💡💡💡listdir()函数，列出目录函数，列出指定目录下的所有文件和子目录，返回一个列表。

import os                       # os模块，提供了许多与操作系统交互的函数。
path = '/Users/young/PycharmProjects/pythonProject'
files = os.listdir(path)  # 列出指定目录下的所有文件和子目录，返回一个列表。
print(files)  # ['test.txt', 'test.py', 'test.py']
# listdir()函数，第一个参数是一个字符串，表示目录的路径，返回一个列表。
# listdir()函数，可以用来列出指定目录下的所有文件和子目录。
# listdir()函数，可以用来判断一个目录是否存在，如果存在，则返回True，否则返回False。

# 53.💡💡💡chr()函数，字符函数，将一个整数转换为对应的字符，返回一个字符串。

number = 65
char = chr(number)  # 将一个整数转换为对应的字符，返回一个字符串。
print(char)  # A
# chr()函数，第一个参数是一个整数，表示字符的Unicode码点，返回一个字符串。

# chr()函数，可以用来将一个整数转换为对应的字符。
# 例子：
number = 97
char = chr(number)
print(char)  # a

# chr()函数，可以用来生成Unicode字符。
# chr()函数，可以用来生成特殊字符，比如制表符、换行符等。
# chr()函数，可以用来生成控制字符，比如回车、换行、制表符等。
# chr()函数，可以用来生成ASCII字符，比如A、B、C、D等。
# chr()函数，可以用来生成Unicode字符，比如汉字、日文、韩文等。

# 例子：
# 生成一个汉字字符：
char = chr(0x4e2d)
print(char)  # 中

# 生成一个日文字符：
char = chr(0x65e5)
print(char)  # 日

# 生成一个韩文字符：
char = chr(0xd55c)
print(char)  # 韩

# 生成一个特殊字符：
char = chr(0x0009)
print(char)  # 制表符
# 生成一个特殊字符：
char = chr(0x000a)
print(char)  # 换行符
# 生成一个特殊字符：
char = chr(0x000d)
print(char)  # 回车符
# 生成一个特殊字符：
char = chr(0x000b)
print(char)  # 垂直制表符
# 生成一个特殊字符：
char = chr(0x000c)
print(char)  # 换页符

# 54.💡💡💡ord()函数，字符函数，将一个字符转换为对应的整数，返回一个整数。

char = 'A'
number = ord(char)  # 将一个字符转换为对应的整数，返回一个整数。
print(number)  # 65
# ord()函数，第一个参数是一个字符串，表示字符，返回一个整数。
# ord()函数，可以用来将一个字符转换为对应的整数。


# 55.💡💡💡bin()函数，将一个整数转换为二进制字符串，返回一个字符串。

number = 10
binary = bin(number)  # 将一个整数转换为二进制字符串，返回一个字符串。‼️binary意思是二进制。
print(binary)  # 0b1010
# bin()函数，第一个参数是一个整数，表示要转换的整数，返回一个字符串。
# bin()函数，可以用来将一个整数转换为二进制字符串。

# 56.💡💡💡hex()函数，将一个整数转换为十六进制字符串，返回一个字符串。

number = 255
hexadecimal = hex(number)  # 将一个整数转换为十六进制字符串，返回一个字符串。‼️hexadecimal意思是十六进制。
print(hexadecimal)  # 0xff
# hex()函数，第一个参数是一个整数，表示要转换的整数，返回一个字符串。
# hex()函数，可以用来将一个整数转换为十六进制字符串。
# hex()函数，可以用来将一个整数转换为十六进制字符串，比如0xff、0x1a等。

# 57.💡💡💡otc()函数，将一个整数转换为八进制字符串，返回一个字符串。

number = 8
octal = oct(number)  # 将一个整数转换为八进制字符串，返回一个字符串。‼️octal意思是八进制。
print(octal)  # 0o10
# oct()函数，第一个参数是一个整数，表示要转换的整数，返回一个字符串。
# oct()函数，可以用来将一个整数转换为八进制字符串。
# oct()函数，可以用来将一个整数转换为八进制字符串，比如0o10、0o20等。


# 58.💡💡💡frozenset()函数，将一个可迭代对象转换为不可变集合，返回一个不可变集合。

numbers = [1, 2, 3, 4, 5]
frozen_numbers = frozenset(numbers)  # 将一个可迭代对象转换为不可变集合，返回一个不可变集合。
print(frozen_numbers)  # frozenset({1, 2, 3, 4, 5})
# frozenset()函数，第一个参数是一个可迭代对象，表示要转换的可迭代对象，返回一个不可变集合。
# frozenset()函数，可以用来将一个可迭代对象转换为不可变集合。
# frozenset()函数，可以用来创建一个不可变集合，比如frozenset({1, 2, 3, 4, 5})。

# 59.💡💡💡bytes()函数，将一个字符串转换为字节串，返回一个字节串。

string = 'Hello, World!'
bytes_string = bytes(string, encoding='utf-8')  # 将一个字符串转换为字节串，返回一个字节串。
                # encoding='utf-8'表示使用utf-8编码。
print(bytes_string)  # b'Hello, World!'
# bytes()函数，第一个参数是一个字符串，表示要转换的字符串，返回一个字节串。
# bytes()函数，可以用来将一个字符串转换为字节串。
# bytes()函数，可以用来将一个字符串转换为字节串，比如b'Hello, World!'。
# bytes()函数，可以用来将一个字符串转换为字节串，比如b'\xe4\xbd\xa0\xe5\xa5\xbd'。

# 60.💡💡💡ascii()函数，将一个字符串转换为ASCII码，返回一个字符串。

string = 'Hello, World!'
ascii_string = ascii(string)  # 将一个字符串转换为ASCII码，返回一个字符串。
print(ascii_string)  # 'Hello, World!'
print(type(string))# <class 'str'
print(type(ascii_string))# <class 'str'>

# ascii()函数，第一个参数是一个字符串，表示要转换的字符串，返回一个字符串。
# ascii()函数，可以用来将一个字符串转换为ASCII码。
# ascii()函数，可以用来将一个字符串转换为ASCII码，比如'Hello, World!'。
# ascii()函数，可以用来将一个字符串转换为ASCII码，比如'\xe4\xbd\xa0\xe5\xa5\xbd'。

# 61.💡💡💡exec()函数，执行函数，执行一个字符串中的Python代码，返回None。

code = '''
for i in range(5):
    print(i)
'''
exec(code)  # 执行一个字符串中的Python代码，返回None。


# 62.💡💡💡format()函数，格式化函数，将一个字符串按照指定的格式进行格式化，返回一个字符串。

name = 'Tom'
age = 18
height = 1.75
info = 'My name is {}, I am {} years old, and my height is {} meters.'.format(name, age, height)
print(info)  # My name is Tom, I am 18 years old, and my height is 1.75 meters.
# format()函数，第一个参数是一个字符串，表示要格式化的字符串，返回一个字符串。
# format()函数，可以用来将一个字符串按照指定的格式进行格式化。
# format()函数，可以用来将一个字符串中的占位符替换为指定的值。
# format()函数，可以用来将一个字符串中的占位符替换为指定的值，比如{}、{0}、{1}等。