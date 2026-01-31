
'''
print(3, [1, 2, 3], {'name': 'David'}) # 一次打印多个对象

print(1, 2, 'x', 'y', sep='*')      # sep参数用于设置多个对象之间的分隔符, sep='*'表示用*号分隔

for item in [1, 2, 'x', 'y']:
    print(item, end=',')             # end参数用于设置打印结束时的字符, end=','表示打印结束后用逗号分隔
    

with open(r'd:\print_out.txt', 'w') as fp: # r表示原始字符串，'w'表示写入模式
    print(1, 2, 'x', 'y', sep='*', file=fp) # file参数用于设置打印的目标文件
'''


import time

def printer(text, delay=0.2): # delay参数用于设置打印的延迟时间,默认为0.2秒
    """打字机效果"""

    for c in text:
        print(c, end='', flush=True)  # flush=True表示立即刷新缓冲区，避免延迟
        time.sleep(delay)
    print()      # 换行
                    # 👆上面这段代码是打印函数，可以用来打印出一些文字，
                    # 比如“Hello World!”，也可以用来打印出一些数字，比如“1234567890”。
'''
# 用例：
printer_1 = printer('Hello World!', 0.5)    # 0.5秒打印一个字符
printer_2 = printer('1234567890', 0.9)      # 0.9秒打印一个字符
                    # 👆上面这段代码是调用打印函数，可以打印出“Hello World!”和“1234567890”

print(printer_1, printer_2) # 打印出打印函数的返回值

                # 如果要保存函数的"效果"而不是返回值，可以这样做：
print("上面已经完成了逐字打印的效果")
'''


def waiting(cycle=20, delay=0.2):
    """旋转式进度指示"""
    for i in range(cycle):                # cycle参数用于设置打印的周期数,默认为20
        for ch in ['-', '\\', '|', '/']:        # ch参数用于设置打印的字符,默认为'-', ['-', '\\', '|', '/']表示打印出'-', '\', '|', '/'这四个字符
            print('\b%s' % ch, end='', flush=True)  # \b 表示退格符，\b%s 表示在当前位置打印一个字符，并退格
            time.sleep(delay)           # delay参数用于设置打印的延迟时间,默认为0.2秒
            print()
'''
# 用例：
kk_0 = waiting(10, 0.1)  # 10个周期，每个周期0.1秒
print(kk_0)
'''

def cover(cycle=100, delay=0.2):
    """覆盖式打印效果"""

    for i in range(cycle):
        s = '\r%d'%i  # \r 表示回车符，%d 表示整数，\r%d 表示在当前位置打印一个整数，并回车
        print(s.ljust(3), end='', flush=True)  # ljust(3) 表示左对齐，宽度为3
        time.sleep(delay)  # delay参数用于设置打印的延迟时间,默认为0.2秒
        print()
'''
# 用例：
kk_1 = cover(100, 0.1)  # 100个周期，每个周期0.1秒
print(kk_1)
'''

if __name__ == '__main__':  # 如果是直接运行该文件，则执行以下代码
    printer('玄铁重剑，是金庸小说笔下第一神剑，持之则无敌于天下。哈哈哈哈!!!')
    waiting(5)  # 20个周期，每个周期0.2秒
    cover(10)  # 100个周期，每个周期0.2秒