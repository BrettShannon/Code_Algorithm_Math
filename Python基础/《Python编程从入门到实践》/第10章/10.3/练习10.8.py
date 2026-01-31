from pathlib import Path # 

path_1 = Path('cat.txt') # 创建一个Path对象
path_2 = Path('dog.txt')

try:
    print(Path.read_text(path_1)) # 读取文件内容
    print(Path.read_text(path_2))

except FileNotFoundError:     # 如果文件不存在，则抛出异常
    print('文件不存在')

      

      