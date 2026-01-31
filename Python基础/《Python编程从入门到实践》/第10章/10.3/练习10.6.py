'''
user_input = input('enter two numbers')
for num_1, num_2 in user_input:
    num_1 = int(user_input)
    num_2 = int(user_input)
    return num_1 + num_2

try:
    print(num_1 + num_2)

except ValueError:
    print('invalid input')
'''

# deepseek:

user_input = input('Enter two numbers separated by space: ')
try:
    # 分割输入并转换为整数
    num_1, num_2 = map(int, user_input.split())
    # split()函数将字符串分割成列表，   
    # map() 函数将一个函数应用于一个或多个可迭代对象，并返回一个迭代器。
    # 在这里，它将int()函数应用于split()函数返回的列表中的每个元素，将字符串转换为整数。
    # int()函数将字符串转换为整数
    print(f"The sum is: {num_1 + num_2}")
except ValueError:
    print('Invalid input. Please enter two integers separated by space.')

