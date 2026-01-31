'''
gen = (x ** 2 for x in range(100))

# 上面的代码相当于👇：

def _make_gen():
    for x in range(100):
        yield x ** 2
gen = _make_gen()

'''

'''
a = sum(x ** 2 for x in range(100))
print(a)

b = dict((i, i ** 2) for i in range(5))
print(b)
'''

# itertools 模块
import itertools
first_letter = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert']