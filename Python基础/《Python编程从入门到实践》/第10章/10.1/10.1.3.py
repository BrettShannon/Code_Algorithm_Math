from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

print(contents) # 做个实验，看看读取的内容是什么样的
print('\n')

lines = contents.splitlines() 
              # 👆splitlines() 方法用于将字符串按行分割，返回一个列表，其中每个元素是文件的一行。（取消换行符）
print(lines)
# 这段代码的作用是读取一个文本文件的内容，并将其按行分割后存储在一个列表中。
print('\n')

for line in lines:
    print(line)
# 这段代码的作用是读取一个文本文件的内容，并将其按行分割后逐行打印出来。
# 具体步骤如下：
# 1. 导入`Path`类：从`pathlib`模块中导入`Path`类，用于处理文件路径。
# 2. 创建`Path`对象：使用`Path`类创建一个对象，表示文件的路径。
# 3. 读取文件内容：使用`read_text()`方法读取文件的全部内容，并将其存储在变量`contents`中。
# 4. 按行分割内容：使用`splitlines()`方法将文件内容按行分割，返回一个列表`lines`，每个元素是文件的一行。
# 5. 遍历并打印每一行：使用`for`循环遍历`lines`列表中的每一行，并将其打印出来。


