
# 操作多个变量，比如调换两个变量所指向的值：

# # 变量交换
# author, reader = 'piglei', 'raymond'     # 定义变量
# # 交换变量的值
# author, reader = reader, author     # 打印变量的值
# print(reader)  # 输出: piglei

# 0.1 变量解包
# username = ['piglei', 'raymond']
# # 👇注意：左侧变量的个数必须和待展开的列表长度相等，否则会报错
# author, reader = username  # 解包列表
# print(author)  # 输出: piglei
# print(reader)  # 输出: raymond


# attrs = [1, ['piglei', 100]] # 定义列表
# user_id, (username, score) = attrs  # 解包列表

# print(user_id)  # 输出: 1
# print(username)  # 输出: piglei
# print(score)  # 输出: 100


# 👇*fruits 会将列表中间的元素全部解包到 fruits 中
# data = ['piglei', 'apple', 'orange', 'banana', 100]
# username, *fruits, score = data  # 解包列表 
# print(username)  # 输出: piglei
# print(fruits)  # 输出: ['apple', 'orange', 'banana']
# print(score)  # 输出: 100

# 👇以下两种变量赋值方式完全等价
# data = ['piglei', 'apple', 'orange', 'banana', 100]
# username, *fruits, score = data  # 解包列表
# username, fruits, score = data[0], data[1:-1], data[-1]  # 解包列表



for username, score in [
    ('piglei', 100),
    ('raymond', 99)
    ]:

    print(username)  # 输出: piglei 100

# 0.2 单下划线变量名_