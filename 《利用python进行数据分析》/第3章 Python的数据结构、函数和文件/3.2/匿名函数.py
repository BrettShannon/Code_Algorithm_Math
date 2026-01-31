'''
def short_function(x):
    return x * 2

equiv_anon = lambda x: x * 2 # 等价的匿名函数
# 这是一个等价的匿名函数
print(short_function(5))  # 输出: 10
'''

'''
def apply_to_list(some_list, f):
    return [f(x) for x in some_list] # 应用函数到列表中的每个元素

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2) # 输出: [8, 0, 2, 10, 12]
# 这是一个匿名函数的应用示例
# 通过使用 lambda 函数，我们可以在不定义正式函数的情况下实现相同的功能
print(apply_to_list(ints, lambda x: x * 2))  # 输出: [8, 0, 2, 10, 12]
'''

'''
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']

strings.sort(key=lambda x: len(set(list(x)))) # 按照字符串中唯一字符的数量排序
# set() 将列表转换为集合，去除重复字符
# list(x) 将字符串转换为字符列表
# len() 计算唯一字符的数量
# sort() 方法对列表进行排序, 排序原则是按照字符串中唯一字符的数量进行排序
# 这里的 lambda 函数用于指定排序的关键字
# 结果是按照字符串中唯一字符的数量进行排序

print(strings)  # 输出: ['foo', 'bar', 'abab', 'aaaa', 'card']
'''

'''柯里化：部分参数应用'''

def add_number(x, y):
    return x + y

# 通过上面这个函数，我们可以派生出一个新的函数——add_five，它用于对其参数加5:
add_five = lambda y: add_number(5, y)  # 柯里化函数
# 这里的 lambda 函数接受一个参数 y，并将其与 5 相加
# 这相当于创建了一个新的函数，它将 5 作为第一个参数，y 作为第二个参数
# 这种方式可以让我们创建更具体的函数，而不需要重复编写完整的函数体
print(add_five(10))  # 输出: 15
# 这里的 add_five 函数将 5 和 10 相加，结果是 15
# 这种方式可以让我们创建更具体的函数，而不需要重复编写完整的函数体
# 这种技术在函数式编程中非常有用，可以让我们创建更灵活和可重用的函数


from functools import partial
# 使用 functools.partial 来实现柯里化
add_five = partial(add_number, 5)  # 使用 functools.partial 创建一个新的函数
# 这里的 partial 函数接受一个函数和一些参数，并返回一个新的函数
# 这个新的函数将自动将 5 作为第一个参数传递给 add_number 函数
print(add_five(10))  # 输出: 15
# 这里的 add_five 函数将 5 和 10 相加，结果是 15