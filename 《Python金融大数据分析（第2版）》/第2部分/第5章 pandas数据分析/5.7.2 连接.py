import pandas as pd
import numpy as np

data = np.random.standard_normal((10, 2))   # 生成10行2列的随机数， standard_normal表示标准正态分布，
                                             # 标准正态分布意思是均值为0，方差为1的正态分布
df = pd.DataFrame(data, columns=['x', 'y'])     # 将数据'data' 转换为DataFrame格式, columns=['x', 'y']表示列名
                # DataFrame格式是pandas库中的一种数据结构，类似于Excel表格，
                # 特点是有行和列，可以存储各种类型的数据，如整数、浮点数、字符串等

df_1 = pd.DataFrame(['100', '200', '300', '400'],
                    index=['a', 'b', 'c', 'd'], # index表示行名
                    columns=['A',])

print(df_1)
print('\n')

df_2 = pd.DataFrame(['200', '150', '50'],
                    index=['f', 'b', 'd'],
                    columns=['B',])
print(df_2)
print('\n')

print(df_1.join(df_2)) # join()函数用于连接两个DataFrame，默认情况下是按行连接，即纵向连接
                    # 输出结果只有4行，也就是 🌟【df_1的行数】，因为df_2中行名'f'在df_1中不存在，所以没有合并。
                    # 输出结果中，df_1和df_2中行名相同的行会合并在一起
print('\n')

print(df_2.join(df_1)) # join()函数用于连接两个DataFrame，默认情况下是按行连接，即纵向连接
                        # 输出结果只有3行，也就是 🌟【df_2的行数】，因为df_1中行名'a'在df_2中不存在，所以没有合并。
print('\n')

print(df_1.join(df_2, how='left')) # how='left'表示按行连接，即纵向连接，且保留 🌟【df_1的所有行】
print('\n')

print(df_1.join(df_2, how='right')) # how='right'表示按行连接，即纵向连接，且保留 🌟【df_2的所有行】，而且颠倒了两个DataFrame的顺序
print('\n')

print(df_1.join(df_2, how='outer')) # how='outer'表示按行连接，即纵向连接，且保留 🌟【df_1和df_2的所有行】
print('\n')

print(df_1.join(df_2, how='inner')) # how='inner'表示按行连接，即纵向连接，且只保留df_1和df_2中 🌟【行名相同的行】
print('\n')

df_3 = pd.DataFrame()  # 创建一个空的DataFrame
print(df_3)
print('\n')

df_3['A'] = df_1['A'] # 将df_1的'A'列添加到df_3中，就好像变量赋值一样。
print(df_3)
print('\n')

df_3['B'] = df_2 # 将df_2的所有列添加到df_3中，就好像变量赋值一样。 df_2后面没有指定列名，所以会添加df_2的所有列。
print(df_3)
print('\n')

df_3 = pd.DataFrame({'A': df_1['A'], 'B': df_2['B']}) # 创建一个DataFrame，并将df_1的'A'列和df_2的'B'列添加到其中
print(df_3)

# 总结：
# join()函数用于连接两个DataFrame，默认情况下是按行连接，即纵向连接。
# how参数可以指定连接方式，包括'left'、'right'、'outer'和'inner'。
# 'left'表示保留df_1的所有行，'right'表示保留df_2的所有行，'outer'表示保留df_1和df_2的所有行，'inner'表示只保留df_1和df_2中行名相同的行。
# 可以通过指定列名来添加列，也可以通过变量赋值的方式来添加列。
# 可以通过指定列名来创建DataFrame，也可以通过字典的方式来创建DataFrame。