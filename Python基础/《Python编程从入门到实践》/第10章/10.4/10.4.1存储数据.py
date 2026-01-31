from pathlib import Path
import json 
# json模块用于将Python数据类型转换为json格式，或将json格式的数据转换为Python数据类型
# json格式的数据的作用是：将数据存储到文件中，或者从文件中读取数据


# 1.将数据存储到文件中

numbers = [2, 3, 5, 7, 11, 13]

path =Path('numbers.json') # 创建一个文件路径
contents = json.dumps(numbers) # 将数据转换为json格式
path.write_text(contents) # 将数据写入文件

# 2.从文件中读取数据

contents = path.read_text()
numbers = json.loads(contents) # 将json格式的数据转换为Python数据类型,loads函数将json格式的字符串转换为Python数据类型
print(numbers)
