'''
def binary_search(list, item): # 二分查找
    low = 0 # 列表的开始位置
    high = len(list) - 1 # 列表的结束位置

    while low <= high: # 当low <= high时，继续查找
        mid = (low + high) / 2 # 中间位置
        guess = list[mid] # 猜的数字
        if guess == item: # 找到了元素
            return mid
        if guess > item: # 如果猜的数字大了，将high设为mid - 1
            high = mid - 1
        else: # 如果猜的数字小了，将low设为mid + 1
            low = mid + 1
    return None # 没有找到元素

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # 输出：1
print(binary_search(my_list, -1)) # 输出：None
'''

# 👆《算法图解》上的python代码版本太低了

#deepseek修改：

from typing import List, Optional
# typing库作用：为Python提供类型提示，帮助开发者编写更清晰、更易于维护的代码。
# List[int] 表示一个整数列表，Optional[int] 表示一个整数或者None

def binary_search(lst: List[int], item: int) -> Optional[int]: # 二分查找 
    # lst: List[int] 表示参数lst的类型是整数列表，item: int 表示参数item的类型是整数
    # -> Optional[int] 表示返回值类型，Optional[int] 表示返回值可以是int类型或者None
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2  # 整数除法
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))   # (my_list, 3)是调用函数，返回值是1
print('\n')
print(binary_search(my_list, -1))  # 输出：None