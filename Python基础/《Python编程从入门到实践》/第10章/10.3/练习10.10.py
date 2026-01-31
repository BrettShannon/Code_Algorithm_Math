
# deepseek修改：
from pathlib import Path
# 正确用法：先创建Path对象
file_path = Path('learning_python.txt')  # 创建Path实例
contents = file_path.read_text() # 读取文件内容

can_num = contents.count('can')  # 计算单词出现次数
print(can_num)