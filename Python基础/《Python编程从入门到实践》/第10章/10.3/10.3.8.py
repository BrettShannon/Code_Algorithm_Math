# 10.3.8 静默失败
# pass

from pathlib import Path

def count_words(path):
    """计算文件大致包含多少个单词"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass 
    else:
        words = contents.split()  # .split() 方法将字符串分割成单词列表
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'] # 这些文件是经典文学作品

for filename in filenames:
    path = Path(filename)
    count_words(path)