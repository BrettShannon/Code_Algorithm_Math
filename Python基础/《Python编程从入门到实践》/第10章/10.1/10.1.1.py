# 10.1.1 读取文件的全部内容

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)
