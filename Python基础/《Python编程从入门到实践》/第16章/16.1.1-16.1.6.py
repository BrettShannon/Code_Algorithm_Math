from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('/Users/mac/Documents/✏️学习记录：编程、算法、数学/《Python编程从入门到实践》/Python蟒蛇书书源代码文件/chapter_16/the_csv_file_format/weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()     # 读取文件内容，按行分割

reader = csv.reader(lines)  # 创建csv读取器对象
                # lines参数为文件内容,按行分割,返回一个列表,reader()函数用于读取csv文件,参数为文件内容。
header_row = next(reader) # next()函数用于获取可迭代对象的下一个元素,参数为可迭代对象,返回可迭代对象的下一个元素。
# print(header_row)


# 16.1.2 打印文件头及其位置
'''
for index, column_header in enumerate(header_row): # enumerate()函数返回一个可迭代对象,包含索引和值
    print(index, column_header)
print()
'''

# 16.1.3 提取并读取数据

# 提取最高温度
'''
highs = []
for row in reader:
    high = int(row[4]) # row[3]表示第四列,即最高温度, int()函数将字符串转换为整数
    highs.append(high) # 将最高温度添加到列表中

print(highs)
'''

# 16.1.4 绘制温度图


#  根据最高温度绘制图形
'''
plt.style.use('seaborn-v0_8')   # 新版本Matplotlib中的seaborn样式名称:'seaborn-v0_8'
                             # 使用seaborn样式,使图形更美观,
                    # seaborn样式是matplotlib内置的一种样式,可以直接使用，无需下载，只需在代码中添加plt.style.use('seaborn')即可。
fig, ax = plt.subplots() 
                    # 创建一个图形对象和一个子图对象, fig表示整个图形, ax表示子图,即图形中的一个部分,可以理解为图形中的一个窗口。
ax.plot(highs, c='red') # 绘制最高温度的折线图, c表示颜色, 'red'表示红色

# 设置图形的格式
ax.set_title("Daily high temperatures, July 2021", fontsize=24) 
                # 设置标题, fontsize表示字体大小, set_title()函数用于设置图形的标题,参数为标题的字符串。
ax.set_xlabel('', fontsize=16) # 设置x轴标签, ''表示不显示标签, fontsize表示字体大小。
ax.set_ylabel("Temperature (F)", fontsize=16) # 设置y轴标签, fontsize表示字体大小。
ax.tick_params(axis='both', which='major', labelsize=16) 
            # 设置刻度标签的字体大小, axis表示轴, 'both'表示x轴和y轴, 
            # which表示刻度类型, 'major'表示主要刻度, labelsize表示字体大小。
            # tick_params()函数用于设置刻度标签的格式,参数为轴、刻度类型和字体大小。

# plt.show() # 显示图形
'''

# 16.1.5 datatime模块

from datetime import datetime
first_data = datetime.strptime('2021-07-01', '%Y-%m-%d') 
                            # 将字符串转换为日期对象, %Y-%m-%d表示日期格式,即年-月-日
                            # strptime()函数用于将字符串转换为日期对象,参数为字符串和日期格式。
# print(first_data)


# 16.1.6 在图中添加日期

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
