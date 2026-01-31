from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 这段代码的作用是读取一个文本文件的内容，并将其按行分割后存储在一个字符串中。
# 具体步骤如下：
# 1. 导入`Path`类：从`pathlib`模块中导入`Path`类，用于处理文件路径。
# 2. 创建`Path`对象：使用`Path`类创建一个对象，表示文件的路径。
# 3. 读取文件内容：使用`read_text()`方法读取文件的全部内容，并将其存储在变量`contents`中。
# 4. 按行分割内容：使用`splitlines()`方法将文件内容按行分割，返回一个列表`lines`，每个元素是文件的一行。
# 5. 遍历每一行：使用`for`循环遍历`lines`列表中的每一行。
# 6. 去除每一行的空格：使用`strip()`方法去除每一行的前后空格，并将结果添加到字符串`pi_string`中。
# 7. 打印字符串：打印最终的字符串`pi_string`，它包含了文件中所有行的内容。
# 8. 打印字符串长度：打印字符串`pi_string`的长度，表示文件中所有行的字符总数。

