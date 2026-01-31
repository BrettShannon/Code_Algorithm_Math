from pathlib import Path
import json
'''
username = input("What is your name? ")

path = Path("username.json") # 创建一个路径对象
contents = json.dumps(username) # 将字符串转换为json格式
path.write_text(contents) # 将json格式的字符串写入文件

print(f"We'll remember you when you come back, {username}")
'''


# 向名字已被存储的用户发出问候：
'''
path = Path("username.json")
contents = path.read_text() # 读取文件内容,返回字符串
username = json.loads(contents) # 将json格式的字符串转换为字符串
# loads()函数将json格式的字符串转换为python对象,这里转换为字符串

print(f"Welcome back, {username}")

print(contents)
'''


path = Path("numbers.json")
if path.exists(): # 检查文件是否存在,exists()函数返回布尔值
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}")
else:
    username = input("What is your name? ")
    contents = json.dumps(username) # 将字符串转换为json格式, json.dumps()函数将python对象转换为json格式的字符串
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}")