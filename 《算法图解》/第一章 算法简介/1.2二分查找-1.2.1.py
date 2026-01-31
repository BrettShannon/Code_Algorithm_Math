def binary_search(list, item): # list为列表，item为要查找的元素
    low = 0
    high = len(list) - 1

    while low <= high: # 只要范围没有缩小到只包含一个元素，就继续查找
        mid = (low + high) // 2 # 计算中间元素的索引
        guess = list[mid] # [] 符号的意思是取列表中索引为mid的元素

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None # 注意缩进长短


# 测试：
my_list = [1, 3, 5, 7, 9] # 列表

print(binary_search(my_list, 3))  # 输出: 1, 索引从0开始，所以3在索引1的位置
print()
print(binary_search(my_list, -1))  # 输出: None, -1不在列表中