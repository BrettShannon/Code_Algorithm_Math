from pathlib import Path

# path = Path('/Users/mac/Documents/💻编程/《从入门到精通》学习/chapter_10/10.3/alice.txt')
path = Path('alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # 计算文件大致包含多少个单词
    words = contents.split() # 将字符串拆分为单词列表
    num_words = len(words) # 计算单词数量
    print(f"The file {path} has about {num_words} words.")
