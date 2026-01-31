from pathlib import Path
import json

def greet_user():
    """问候用户，并指出其名字。"""
    path = Path("username.json")
    if path.exists():
        contents = path.read_text() # 读取文件内容, 将JSON数据转换为Python数据,数据格式为字符串
        username = json.loads(contents) # 将文件内容转换为Python数据
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username) # 将Python数据转换为JSON格式
        path.write_text(contents) # 将JSON数据写入文件
        print(f"We'll remember you when you come back, {username}!")

greet_user()

# 重构以上函数代码👇

from pathlib import Path
import json

def get_stored_username():
    """如果存储了用户名，就获取它。"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None # 如果文件不存在，就返回None
    
def get_new_username(path):
    """提示用户输入用户名，并将其返回。"""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents) # 将JSON数据写入文件
    return username
    
def greet_user():
    """问候用户，并指出其名字。"""
    path = Path("username.json")
    username = get_stored_username(path) # 调用函数
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()