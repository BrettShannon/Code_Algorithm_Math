from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

path = Path('/Users/mac/Documents/✏️学习记录：编程、算法、数学/《Python编程从入门到实践》/Python蟒蛇书书源代码文件/chapter_16/the_csv_file_format/weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()     # 读取文件内容，按行分割

reader = csv.reader(lines)  # 创建csv读取器对象, lines参数为文件内容,按行分割,返回一个列表
header_row = next(reader) # 调用next()函数,返回csv文件的第一行,即文件头
# print(header_row)

first_data = datetime.strptime('2021-07-01', '%Y-%m-%d') 
                            # 将字符串转换为日期对象, %Y-%m-%d表示日期格式,即年-月-日
                            # strptime()函数用于将字符串转换为日期对象,参数为字符串和日期格式。
# print(first_data)

# 16.1.6 在图中添加日期
'''
# 提取日期和最高温度
dates, highs = [], [] # 同时初始化两个空列表, dates用于存储日期, highs用于存储最高温度
                        # ————同时定义两个变量，python竟然可以如此优雅，太厉害了。

for row in reader:              # 遍历csv文件中的每一行,reader是一个可迭代对象,包含csv文件中的每一行
    current_date = datetime.strptime(row[2], '%Y-%m-%d') # 将字符串转换为日期对象
    high = int(row[4]) # 将字符串转换为整数
    dates.append(current_date) # 将日期对象添加到列表中
    highs.append(high) # 将最高温度添加到列表中

# 根据数据绘图
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots() # 创建图形对象和子图对象，fig表示整个图形，ax表示子图，即图形中的一个部分，可以理解为图形中的一个窗口。
                    # subplots（）函数用于创建图形对象和子图对象，参数为子图的行数和列数，默认为1行1列。
ax.plot(dates, highs, c='red') # 绘制最高温度的折线图，c表示颜色，'red'表示红色

# 设置图形的格式
ax.set_title("Daily high temperatures, July 2021", fontsize=24) # 设置标题，fontsize表示字体大小，set_title()函数用于设置图形的标题，参数为标题的字符串。
ax.set_xlabel('', fontsize=16) # 设置x轴标签，''表示不显示标签，fontsize表示字体大小。
fig.autofmt_xdate() # 自动格式化x轴的日期标签，使日期标签不重叠
ax.set_ylabel("Temperature (F)", fontsize=16) # 设置y轴标签，fontsize表示字体大小。
ax.tick_params(axis='both', which='major', labelsize=16) # 设置刻度标签的字体大小，axis表示轴，'both'表示x轴和y轴，which表示刻度类型，'major'表示主要刻度，labelsize表示字体大小。

plt.show() # 显示图形
'''

# 16.1.7 涵盖更长的时间

path= Path('/Users/mac/Documents/✏️学习记录：编程、算法、数学/《Python编程从入门到实践》/Python蟒蛇书书源代码文件/chapter_16/the_csv_file_format/weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()     # 读取文件内容，按行分割

reader = csv.reader(lines)  # 创建csv读取器对象, lines参数为文件内容,按行分割,返回一个列表
header_row = next(reader) # 调用next()函数,返回csv文件的第一行,即文件头

'''
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots() # 创建图形对象和子图对象，fig表示整个图形，ax表示子图，即图形中的一个部分，可以理解为图形中的一个窗口。
                    # subplots（）函数用于创建图形对象和子图对象，参数为子图的行数和列数，默认为1行1列。

dates, highs = [], [] # 同时初始化两个空列表, dates用于存储日期, highs用于存储最高温度
                        # ————同时定义两个变量，python竟然可以如此优雅，太厉害了。
for row in reader:              # 遍历csv文件中的每一行,reader是一个可迭代对象,包含csv文件中的每一行
    current_date = datetime.strptime(row[2], '%Y-%m-%d') # 将字符串转换为日期对象
    high = int(row[4]) # 将字符串转换为整数
    dates.append(current_date) # 将日期对象添加到列表中
    highs.append(high) # 将最高温度添加到列表中
    
ax.plot(dates, highs, c='red') # 绘制最高温度的折线图，c表示颜色，'red'表示红色


# 设置绘图的格式：
ax.set_title("Daily high temperatures, 2021", fontsize=24) #ax是子图对象
ax.set_xlabel('', fontsize=16)          # 设置x轴标签，''表示不显示标签，fontsize表示字体大小。

# plt.show() # 显示图形
'''

# 16.1.8 再绘制一个数据系列
'''
dates, highs, lows = [], [], [] # 同时初始化三个空列表, dates用于存储日期, highs用于存储最高温度, lows用于存储最低温度
for row in reader:              # 遍历csv文件中的每一行,reader是一个可迭代对象,包含csv文件中的每一行
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)
'''

# 提取日期、最高温度和最低温度
dates, highs, lows = [], [], []
for row in reader:              # 遍历csv文件中的每一行,reader是一个可迭代对象,包含csv文件中的每一行
    current_date = datetime.strptime(row[2], '%Y-%m-%d') 
            # strptime(row[2]）将字符串转换为日期对象， row[2]表示csv文件中的第三列，即日期列。
    high = int(row[4]) # 将字符串转换为整数，row[4]表示csv文件中的第五列，即最高温度列。
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# 根据数据绘图

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots() # subplots（）函数用于创建图形对象和子图对象，参数为子图的行数和列数，默认为1行1列。
                        # 创建图形对象和子图对象，fig表示整个图形，ax表示子图，即图形中的一个部分，可以理解为图形中的一个窗口。
'''
ax.plot(dates, highs, c='red', alpha=0.5) # 绘制最高温度的折线图，c表示颜色，'red'表示红色，alpha表示透明度，0.5表示50%的透明度。
ax.plot(dates, lows, c='blue', alpha=0.5) # 绘制最低温度的折线图，c表示颜色，'blue'表示蓝色，alpha表示透明度，0.5表示50%的透明度。
'''

# 设置绘图的格式：
ax.set_title("Daily high and low temperatures, 2021", fontsize=24) #ax是子图对象
# plt.show() # 显示图形

# 16.1.9 给数据集添加颜色

ax.plot(dates, highs, c='red', alpha=0.5) # 绘制最高温度的折线图，c表示颜色，'red'表示红色，alpha表示透明度，0.5表示50%的透明度。
ax.plot(dates, lows, c='blue', alpha=0.5) # 绘制最低温度的折线图，c表示颜色，'blue'表示蓝色，alpha表示透明度，0.5表示50%的透明度。
ax.fill_between(dates, highs, lows, color='blue', alpha=0.1) 
            # fill_between()函数用于填充两个数据系列之间的区域，参数为x轴数据、y轴数据、颜色、透明度。
plt.show() # 显示图形