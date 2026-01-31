# deepseek :
while True:
    user_input = input('Enter two integers separated by space: ')
    parts = user_input.split() # 分割输入
    print(parts)
    
    # 验证输入
    if len(parts) == 2 and all(part.isdigit() for part in parts): 
        # len(parts) == 2 检查输入是否为两个部分, len()函数返回字符串的长度
        # all()函数检查所有元素是否为真, isdigit()函数检查字符串是否为数字
        num1, num2 = map(int, parts) # 将字符串转换为整数, map()函数将函数应用于可迭代对象的每个元素
        print(f"The sum is: {num1 + num2}")
        break
    else:
        print('Invalid input. Please enter exactly two integers separated by space.')

# 代码解释:
# 1. 使用while循环来不断接受用户输入, 直到输入有效为止。
# 2. 使用input()函数来接受用户输入, 并使用split()函数将输入分割为两个部分。
# 3. 使用len()函数和all()函数来验证输入是否为两个整数, 如果不是, 则打印错误信息并继续循环。
# 4. 使用map()函数将字符串转换为整数, 并将结果存储在num1和num2变量中。
# 5. 打印两个整数的和, 并使用break语句来结束循环。
# 代码运行结果:
# Enter two integers separated by space: 3 4
# The sum is: 7
# Enter two integers separated by space: 3.5 4
# Invalid input. Please enter exactly two integers separated by space.
# Enter two integers separated by space: 3 4 5
# Invalid input. Please enter exactly two integers separated by space.

# all()的用法:
# all()函数用于检查可迭代对象中的所有元素是否都为真, 如果所有元素都为真, 则返回True, 否则返回False。
# 例如, all([1, 2, 3])返回True, all([1, 0, 3])返回False。
# all()函数可以用于检查列表、元组、字符串等可迭代对象中的所有元素是否都为真。
# 例如, all(['a', 'b', 'c'])返回True, all(['a', '', 'c'])返回False。
# all()函数还可以用于检查列表、元组、字符串等可迭代对象中的所有元素是否都为非空字符串。
# 例如, all(['a', 'b', 'c'])返回True, all(['a', '', 'c'])返回False。
# all()函数还可以用于检查列表、元组、字符串等可迭代对象中的所有元素是否都为非空字符串。
# 例如, all(['a', 'b', 'c'])返回True, all(['a', '', 'c'])返回False。

# 可迭代对象:
# 可迭代对象是指可以遍历的对象, 例如列表、元组、字符串、字典等。
# 可迭代对象可以使用for循环来遍历, 例如:
# for i in [1, 2, 3]:
#     print(i)
# for i in ('a', 'b', 'c'):
#     print(i)
# for i in 'abc':
#     print(i)
# for i in {'a': 1, 'b': 2, 'c': 3}.values():
#     print(i)
# 代码运行结果:
# 1
# 2
# 3
# a
# b
# c
# a
# b
# c
# 1
# 2
# 3