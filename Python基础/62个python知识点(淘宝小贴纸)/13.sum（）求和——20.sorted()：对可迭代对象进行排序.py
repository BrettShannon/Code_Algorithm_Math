# 13.sum():返回可迭代对象的总和————求和

number = [1,2,3,4,5,6,7,8,9,10]
total = sum(number)
print(total)
print("---------------")

# 14.max()：返回可迭代对象中的最大值

number = [1,2,3,4,5,6,7,8,9,10]
maximum= max(number)
print(maximum)
print("---------------")

# 15.min()：返回可迭代对象中的最小值

number = [1,2,3,4,5,6,7,8,9,10]
minimum = min(number)
print(minimum)
print("---------------")

# 16.abs()：返回一个数的绝对值

number = -42
absolute = abs(number)
print(absolute)
print("---------------")

# 17.replace()：替换字符串中的指定字符
st = "i want an apple"
new_st = st.replace("apple","banana")
print(new_st)
print("---------------")

# 18.round()：返回浮点数的四舍五入值

number = 3.1415926
round_number = round(number,2) # 保留两位小数
print(round_number)
print("---------------")

# 19.strip()：将字符串分割成列表

st = "hello"
new_st = st.strip()
print(new_st + "world")
print(type(new_st))
print("---------------")

# 20.sorted()：对可迭代对象进行排序

number = [5, 2, 4, 1, 3]
sorted_numbers = sorted(number)
print(sorted_numbers)
print("---------------")

# 对可迭代对象进行降序排序

number = [5, 2, 4, 1, 3]
sorted_numbers = sorted(number, reverse=True) # 降序排序    reverse=True,表示降序
print(sorted_numbers)
print("---------------")



