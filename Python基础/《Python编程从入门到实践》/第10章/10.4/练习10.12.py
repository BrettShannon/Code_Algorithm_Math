from pathlib import Path
import json

# path = Path ("numbers_you_like.json")
# contents = path.read_text()
# numbers_you_like = json.loads(contents) # 将字符串转换为列表，loads()函数将字符串转换为列表
# print(contents)
# # 输出的内容格式是字符串

path = Path ("numbers_you_like.json")
if path.exists():
    contents = path.read_text() 
    numbers_you_like = json.loads(contents)
    print(f"You have saved some numbers you like. It's {contents}")
else:
    numbers_you_like = [] # 如果文件不存在，则创建一个空列表
    path.write_text(json.dumps(numbers_you_like)) # 将空列表转换为字符串，并写入文件
    print("Enter a number that you like: ")
    number = input() # 输入一个数字
    numbers_you_like.append(number) # 将数字添加到列表中
    path.write_text(json.dumps(numbers_you_like)) # 将列表转换为字符串，并写入文件
    print("You have saved a number you like.")