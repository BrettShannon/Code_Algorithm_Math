# 练习 10.4
from pathlib import Path

# 第一种方法：
# ask = input("Enter your name: ")
# print(ask)
# contents = ask
# # contents = f"{ask}" # 根本不用转换数据类型，因为input（）下的内容都是字符串
# doc = Path('guest.txt')
# doc.write_text(contents)
# print_doc = doc.read_text()
# print(print_doc)

# 第二种方法：

# ask = input("Enter your name: ")
# doc = Path('guest.txt')
# doc.write_text(ask)
# print_doc = doc.read_text()
# print(print_doc)