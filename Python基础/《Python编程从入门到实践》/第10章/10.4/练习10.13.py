'''
from pathlib import Path
import json

def get_user_info(path):
    """如果存储了用户信息，就获取它"""
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    else:
        return None
    
def get_user_name():
    name = input("Enter your name: ")
    path = Path("name.json")
    contents = json.dumps(name)
    path.write_text(contents)
    
def get_user_gender():
    gender = input("Enter your gender: ") # 获取用户输入的性别
    path = Path("gender.json") # 创建一个文件
    contents = json.dumps(gender) # 将性别转换为字符串
    path.write_text(contents)

def get_user_age():
    age = input("Enter your age: ")
    path = Path("age.json")
    contents = json.dumps(age)
    path.write_text(contents)

def greet_user():
    """问候用户，并根据他们是否已存储了用户信息来显示不同的消息"""
    path = Path("user.json")
    user_info = get_user_info(path)
    if user_info:
        print(f"Welcome back, {user_info['name']}!")
    else:
        get_user_name()
        get_user_gender()
        get_user_age()
        user_info = get_user_info(path)
        print(f"Hi {user_info['name']}! We've saved your info to {path}.")
        print(f"We know that you are a {user_info['gender']} and you are {user_info['age']} years old.")

greet_user()
'''

'''
ChatGPT：

你的代码结构已经很好了，分了几个函数，意图清晰。但是目前它存在一个关键逻辑错误，导致 greet_user() 无法获取新用户的信息，并且 user.json 文件其实从未被写入。我们来逐步诊断：

✅ 你当前的代码行为
greet_user() 会检查是否有 "user.json" 文件，如果有就读取并问候；

如果 "user.json" 不存在，它会调用：

get_user_name() ➜ 写入 "name.json"

get_user_gender() ➜ 写入 "gender.json"

get_user_age() ➜ 写入 "age.json"

然后它又尝试从 "user.json" 读取数据。

问题是：你从未创建过 user.json 文件。 所以新用户的信息根本没有合并到这个文件中，导致 user_info 永远是 None，程序逻辑就出错了。

❌ 具体问题汇总
问题	说明
没有写入 user.json	get_user_name() 等函数只写入了各自的文件，没有整合
greet_user() 读取的是不存在的数据结构	你希望它读取包含 name, gender, age 的 JSON 对象，但从未创建它
get_user_info() 假设所有数据都存在于同一个 JSON 文件中，这与实际写法不一致	

✅ 正确做法建议
你应该统一地把 name、gender、age 存入一个字典，然后写入 "user.json"，这样才能一次性存取所有信息。
'''

# ✅ 改进后的代码（推荐版本）

from pathlib import Path
import json

def get_user_info(path):
    """读取用户信息，如果文件存在则返回内容"""
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    else:
        return None

def collect_user_info(path):
    """收集用户信息并写入 user.json 文件"""
    name = input("Enter your name: ")
    gender = input("Enter your gender: ")
    age = input("Enter your age: ")

    user_info = {
        "name": name,
        "gender": gender,
        "age": age
    }

    contents = json.dumps(user_info) # 将字典转换为字符串
    path.write_text(contents) # 将字符串写入文件
    return user_info

def greet_user():
    path = Path("user.json") # 创建一个文件
    user_info = get_user_info(path)
    if user_info:
        print(f"Welcome back, {user_info['name']}!")
        print(f"You are a {user_info['gender']} and you are {user_info['age']} years old.")
    else:
        user_info = collect_user_info(path)
        print(f"Hi {user_info['name']}! We've saved your info to {path}.")
        print(f"We know that you are a {user_info['gender']} and you are {user_info['age']} years old.")

greet_user() # 调用函数


# 讲一下上面代码中的业务逻辑和函数嵌套的逻辑(chatgpt)

'''
很好，我们就来详细讲解你上面那段经过改进后的代码：

---

## 🧠 一、整体**业务逻辑流程**（Business Logic）

这个程序的业务逻辑很简单，分为两个主要部分：

### ✅ 情况 1：已有用户信息（`user.json` 存在）

1. 从文件 `user.json` 中读取用户数据。
2. 如果能成功读取，就打印欢迎语，并显示姓名、性别、年龄。

---

### ✅ 情况 2：第一次运行（文件不存在）

1. 提示用户输入姓名、性别、年龄。
2. 把这些信息打包成一个字典，写入 `user.json`。
3. 打印欢迎信息，告诉用户数据已保存。

---

## 🧩 二、函数结构和**调用嵌套逻辑**

我们一层层展开函数之间是如何配合的：

---

### 1️⃣ `greet_user()` 是**程序入口函数**

它的职责是控制整个“欢迎 + 数据读写”的逻辑流程：

```python
def greet_user():
    path = Path("user.json")
    user_info = get_user_info(path)
    if user_info:
        # 情况 1：读取成功
        ...
    else:
        # 情况 2：没有保存数据
        user_info = collect_user_info(path)
        ...
```

---

### 2️⃣ `get_user_info(path)` 是一个**通用读取函数**

用于尝试从给定路径的文件读取并解析 JSON 数据：

```python
def get_user_info(path):
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    else:
        return None
```

你可以把它理解为：

> “如果这个文件存在，就打开它，看看里面有没有 JSON 数据。”

---

### 3️⃣ `collect_user_info(path)` 是一个**收集+写入数据的函数**

它负责：

* 获取用户输入（`input()`）
* 构建一个字典对象：`{"name": ..., "gender": ..., "age": ...}`
* 将其写入 JSON 文件中（覆盖旧的）

```python
def collect_user_info(path):
    name = input("Enter your name: ")
    gender = input("Enter your gender: ")
    age = input("Enter your age: ")

    user_info = {
        "name": name,
        "gender": gender,
        "age": age
    }

    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info
```

注意这个函数**返回 user\_info 对象**，这样 `greet_user()` 也能继续用它来打印欢迎语。

---

## 🔁 三、函数调用链（嵌套逻辑）

我们可以画一个简洁的流程图来理解调用顺序：

```
greet_user()
 ├── get_user_info(path)
 │    └── 文件存在？读取JSON → 返回 dict / None
 └── if None:
       └── collect_user_info(path)
            └── input() 3次 → 构建 dict → 写入文件 → 返回 dict
```

这个流程具有非常清晰的“主控函数（greet\_user） + 辅助函数（get/collect）”结构。

---

## ✅ 总结重点

| 结构部分                  | 作用          | 特点               |
| --------------------- | ----------- | ---------------- |
| `greet_user()`        | 控制整个业务流程    | 程序入口，调用其他函数      |
| `get_user_info()`     | 从文件读取数据     | 解耦、可复用、判断文件是否存在  |
| `collect_user_info()` | 收集用户输入并保存数据 | 集中写入逻辑，返回结果给主控函数 |

---

如果你想进一步学习结构化编程或 OOP（面向对象），我们还可以把它封装成一个 `UserManager` 类来练习“类”和“对象”的概念。

你想试试升级版吗？👨‍💻💡

'''

# 可以

'''
好嘞！我们来把你当前的代码封装进一个\*\*面向对象（OOP）\*\*的类中，做一个更结构化、易维护的“用户管理器”示范。

---

# 1. 设计思路

* 创建一个 `UserManager` 类
* 属性保存用户文件路径
* 方法包括：

  * 读取用户信息
  * 收集用户信息
  * 打印问候语
  * 入口函数统一调用

---

# 2. 代码示范

```python
from pathlib import Path
import json

class UserManager:
    def __init__(self, filepath="user.json"):
        self.filepath = Path(filepath)
        self.user_info = None

    def load_user_info(self):
        """尝试读取用户信息，如果文件存在返回 dict，否则 None"""
        if self.filepath.exists():
            contents = self.filepath.read_text()
            self.user_info = json.loads(contents)
        else:
            self.user_info = None

    def save_user_info(self):
        """将当前用户信息写入文件"""
        if self.user_info:
            contents = json.dumps(self.user_info, indent=4)
            self.filepath.write_text(contents)

    def collect_user_info(self):
        """交互式收集用户信息"""
        name = input("Enter your name: ")
        gender = input("Enter your gender: ")
        age = input("Enter your age: ")

        self.user_info = {
            "name": name,
            "gender": gender,
            "age": age
        }
        self.save_user_info()

    def greet_user(self):
        """主逻辑：读取用户信息，问候或收集"""
        self.load_user_info()
        if self.user_info:
            print(f"Welcome back, {self.user_info['name']}!")
            print(f"You are a {self.user_info['gender']} and you are {self.user_info['age']} years old.")
        else:
            self.collect_user_info()
            print(f"Hi {self.user_info['name']}! We've saved your info to {self.filepath}.")
            print(f"We know that you are a {self.user_info['gender']} and you are {self.user_info['age']} years old.")

# 程序入口
if __name__ == "__main__":
    manager = UserManager()
    manager.greet_user()
```

---

# 3. 说明

* `__init__`：初始化文件路径，方便后续操作
* `load_user_info`：读取文件并存储在对象属性里
* `save_user_info`：写入当前属性数据
* `collect_user_info`：交互输入，赋值并保存
* `greet_user`：主控流程方法，程序启动调用

---

# 4. 优势

* 代码结构清晰，相关操作都聚合在一个对象里
* 易于扩展，比如后续加“更新信息”或“删除信息”方法
* 实际项目中，更符合Python中面向对象的工程规范

---

你觉得这样面向对象的改写清晰易懂吗？需要我帮你讲讲类和对象的基本概念吗？

'''