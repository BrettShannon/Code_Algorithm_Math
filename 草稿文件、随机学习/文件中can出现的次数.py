from pathlib import Path
print("当前工作目录:", Path.cwd())  # 重点检查这里！ # .cwd()返回当前工作目录
print("文件绝对路径:", Path('learning_python.txt').absolute()) # .absolute()返回文件的绝对路径

file_path = Path('learning_python.txt')
if file_path.exists(): # 检查文件是否存在
    contents = file_path.read_text()
    print(f"'can'出现次数: {contents.count('can')}")
else:
    print(f"文件不存在于: {file_path.absolute()}")