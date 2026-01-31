from pathlib import Path

def count_words(path):
    """计算文件大致包含多少个单词"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()  # .split() 方法将字符串分割成单词列表
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path('learning_python.txt')
count_words(path)


# 分析多个文件：
'''

def count_words(path):
    """计算文件大致包含多少个单词"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()  # .split() 方法将字符串分割成单词列表
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'] # 这些文件是经典文学作品

for filename in filenames:
    path = Path(filename)
    count_words(path)

    # (由于没有'alice.txt','siddhartha.txt', 'moby_dick.txt', 'little_women.txt'这些文件，所以程序并不能运行)
    # (但是这个程序可以用来分析这些文件)
    '''