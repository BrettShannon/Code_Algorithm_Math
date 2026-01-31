# 4.range()：生成一个指定范围内的整数序列
for num in range(1, 5):
    print(num)

print("-----------------")

# 5. str()()：将数据转换为字符串类型

number = 42
string = str(number)
print(string)
print("-----------------")

# 6. int()：将数据转换为整数类型
string = "42"
number = int(string)
print(number)
print("-----------------")

# 7. float()：将数据转换为浮点数类型
string = "3.14"
number = float(string)
print(number)
print("-----------------")

# 8.type()：查看数据类型
print(type(42))
print(type(3.14))
print(type("hello")) # 字符串
print(type(True)) # 布尔值
print(type(None)) # 空值
print(type([1, 2, 3])) # 列表
print(type((1, 2, 3))) # 元组
print(type({"name": "Tom", "age": 18})) # 字典
print(type({"name": "Tom", "age": 18, "gender": "male"})) # 字典
print(type({"name": "Tom", "age": 18, "gender": "male", "hobbies": ["reading", "swimming"]}))
print("-----------------")

# 9.list() ：将数据转换为列表类型
string = "hello"
char_list = list(string)
print(char_list)
print(type(char_list))
print("-----------------")

# 10.tuple()：将数据转换为元组类型
list_data = [1, 2, 3]
tuple_data = tuple(list_data)
print(tuple_data)
print(type(tuple_data))
print("-----------------")

# 11.dict()：将数据转换为字典类型
person = dict(name="Tom", age=18)
print(person)
print(type(person))
print("-----------------")

# 12 set() 创建一个集合对象

numbers =[1,2,3,4,5,6,7,8,9,10]
unique_numbers = set(numbers)
print(unique_numbers)
print(type(unique_numbers))
print("-----------------")

