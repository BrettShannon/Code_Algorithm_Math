from pathlib import Path

# lianxi 10.1

# path = Path('learning_python.txt')
# contents = path.read_text()
# print(contents)

# print('再打一次该内容:')
# lines = contents.splitlines()
# for line in lines:
#     print(line)

# lianxi 10.2
# 示例
# message = "I really like dogs."
# message_1 = message.replace('dog', 'cat')   # .replace()方法可以将dog替换为cat
# print(message_1)

# path = Path('learning_python.txt')
# contents = path.read_text()
# message_2 = contents.replace('Python', 'C')
# print(message_2)

# 练习10.3
# 原file_reader.py文件：

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)

# 练习10.3中省略临时变量lines的程序写法👇：

# path = Path('pi_digits.txt')
# contents = path.read_text()

# for line in contents.splitlines():
#     print(line)