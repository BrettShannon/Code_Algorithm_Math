from pathlib import Path

# cg给的答案：

filename = "guest_book.txt"
print("请输入你的名字（输入 'q' 退出）：")

while True:
    name = input("Name: ")
    if name.lower() == 'q':
        break
    print(f"欢迎你，{name}！")
    with open(filename, 'a', encoding='utf-8') as file:
        # 写入访客的名字到文件
        # 使用 'a' 模式表示追加内容到文件末尾
        # encoding='utf-8' 确保文件使用 UTF-8 编码
        # 这样可以正确处理中文字符
        file.write(f"{name} 访问了本站。\n")
        # 这里的 file.write() 方法用于向文件写入内容
        # 在这里，我们将访客的名字和一条欢迎消息写入文件

'''
ChatGPT 说：
.write() 是 Python 中文件对象的方法，用来向文件写入字符串内容。

✅ 基本语法：

with open("文件名.txt", "w", encoding="utf-8") as file:
    file.write("你好，世界")
这行代码的作用是：
👉 把字符串 "你好，世界" 写入名为 "文件名.txt" 的文件中。
'''