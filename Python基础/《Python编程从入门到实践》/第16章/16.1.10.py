from pathlib import Path    # 导入Path类，用于处理文件路径
from datetime import datetime # 导入datetime模块，用于处理日期和时间
import csv                  # 导入csv模块，用于读取csv文件
import matplotlib.pyplot as plt # 导入matplotlib.pyplot模块，用于绘制图形

path = Path('F:/Code_Algorithm_Math/Python基础/《Python编程从入门到实践》/Python蟒蛇书书源代码文件/chapter_16/the_csv_file_format/weather_data/death_valley_2021_simple.csv')
                                                    # 创建一个Path对象，表示文件路径
lines = path.read_text().splitlines()     # 读取文件内容，按行分割

reader = csv.reader(lines)  # 创建csv读取器对象, lines参数为文件内容,按行分割,返回一个列表,
                            # reader（）函数用于读取csv文件,参数为csv文件路径,返回一个csv读取器对象,reader对象是一个可迭代对象,包含csv文件中的每一行
header_row = next(reader) # 调用next()函数,返回csv文件的第一行,即文件头

for index, column_header in enumerate(header_row): 
                            # enumerate()函数用于将可迭代对象组合为一个索引序列，同时列出数据和数据下标，一般用在for循环当中。
    print(index, column_header) # 输出每一列的索引和列名

dates, highs, lows = [], [], [] # 创建三个空列表，用于存储日期、最高温度和最低温度
for row in reader:              # 遍历csv文件中的每一行,reader是一个可迭代对象,包含csv文件中的每一行
    current_date = datetime.strptime(row[2], '%Y-%m-%d')            # 将日期字符串转换为datetime对象，参数为日期字符串和日期格式
    try:
        high = int(row[3])
        low = int(row[4])
        # 将最高温度和最低温度转换为整数
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        # 将日期、最高温度和最低温度添加到对应的列表中
        
# 根据最低和最高温度绘图：
plt.style.use('seaborn-v0_8')           # 设置绘图风格，参数为风格名称，seaborn-v0_8是seaborn库中的一个风格，用于绘制美观的图形。
fig, ax = plt.subplots()                # subplots（）函数用于创建图形对象和子图对象，参数为子图的行数和列数，默认为1行1列。
                                        # 创建图形对象和子图对象，fig表示整个图形，ax表示子图，即图形中的一个部分，可以理解为图形中的一个窗口。
ax.plot(dates, highs, c='red', alpha=0.5) # 绘制折线图，参数为x轴数据、y轴数据、颜色、透明度。
ax.plot(dates, lows, c='blue', alpha=0.5) # 绘制折线图，参数为x轴数据、y轴数据、颜色、透明度。
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # 填充两个折线之间的区域，参数为x轴数据、y轴数据、填充颜色、透明度。
                                            # fill_between()函数用于填充两个折线之间的区域，参数为x轴数据、y轴数据、填充颜色、透明度。

# 设置绘图的格式

title = f"Daily high and low temperatures, 2021\nDeath Valley, CA"          # 设置标题，参数为标题字符串
ax.set_title(title, fontsize=20) # 设置标题，fontsize表示字体大小，set_title()函数用于设置图形的标题，参数为标题的字符串。
ax.set_xlabel('', fontsize=16) # 设置x轴标签，''表示不显示标签，fontsize表示字体大小。
plt.show() # 显示图形