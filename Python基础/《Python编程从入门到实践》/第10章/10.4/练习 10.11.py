from pathlib import Path
import json

number = input("Enter a number that you like: ") # input()函数用于获取用户输入的字符串

path = Path("numbers_you_like.json") # Path()函数用于创建一个路径对象
contents = json.dumps(number) # json.dump()函数将Python对象转换为JSON格式，并返回一个字符串
path.write_text(contents)

print(path) # 打印路径对象
print(f"I know your favourite number, it's {contents}") # 打印字符串