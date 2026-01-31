# 1.把字符串当做序列来操作：
# 字符串是一种序列类型，意味着你可以对它进行遍历、切片等操作，就像访问一个列表：

# 遍历字符串s:
s = 'Hello, world!'
for c in s:
    print(c)

print()

# 对s进行切片：
print(s[1:3])

# 反转字符串
print(s[::-1])

print(''.join(reversed(s)))
print()

# 2.字符串格式化：
name = 'World'
print(f'Hello,{name}')
print()

username, score = 'piglei', 100
# 1. C语言风格格式化：
print('Welcome %s, your score is %d' % (username, score))
print()
# 2. str.format
print('Welcome {}, your score is {:d}'.format(username, score))
print()
# 3. f-string, 最短最直观
print(f'Welcome {username }, your score is {score:d}')

