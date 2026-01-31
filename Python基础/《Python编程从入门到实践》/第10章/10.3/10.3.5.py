# 10.3.5 处理FileNotFoundError异常

from pathlib import Path
# pathlib是Python标准库中的一个模块，它提供了一种面向对象的方式来处理文件系统路径。
# Path类是pathlib模块中的一个类，它表示一个文件系统路径，可以用于访问和操作文件系统中的文件和目录。

path = Path('/Users/mac/Documents/💻编程/《从入门到精通》学习/chapter_10/10.3/alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

'''
path = Path('alice.txt')
content = path.read_text(encoding='utf-8')

print(content)
'''