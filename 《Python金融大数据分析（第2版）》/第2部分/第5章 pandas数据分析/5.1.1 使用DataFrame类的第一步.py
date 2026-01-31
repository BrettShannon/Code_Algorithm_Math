'''
pandas安装在了解释器找不到的位置👇
deepseek：
解决方法 2：直接指定 Python 解释器路径
bash
# 例如（Windows）：
C:\Python310\python.exe -m pip install pandas

# 例如（macOS/Linux）：
‼️ /usr/local/bin/python3 -m pip install pandas
'''
# /usr/local/bin/python3 -m pip install matplotlib

import pandas as pd

df = pd.DataFrame([10, 20, 30, 40,], # 数据
                  columns=['numbers'], # 列名
                  index = ['a', 'b', 'c', 'd']) # 索引
# 上面的代码创建了一个 DataFrame，其中包含一个名为 'numbers' 的列和一个名为 'a', 'b', 'c', 'd' 的索引。
# DataFrame 类：二维的带标签的数据结构，可以看作是由Series组成的字典（共用同一个索引）

# print(df)

# print(pd.__version__)  # 输出如：2.0.3
'''
print(f"\n{df.index}") # 输出：Index(['a', 'b', 'c', 'd'], dtype='object')

print(f"\n{df.columns}") # 输出：Index(['numbers'], dtype='object')

print(f"\n{df.loc['c']}")
# loc方法用于根据标签选择数据，返回一个Series或DataFrame。

print(f"\n{df.loc[['a', 'd']]}")

print(f"\n{df.iloc[1:3]}")
# iloc方法用于根据位置选择数据，返回一个Series或DataFrame。

print(f"\n{df.sum()}")

print(f"\n{df.apply(lambda x: x ** 2)}") # 使用apply方法，以向量化的方式计算平方值。
# apply方法用于对DataFrame中的每个元素或每列应用一个函数，返回一个Series或DataFrame。

print(f"\n{df ** 2}") n# 使用**运算符，以逐元素的方式计算平方值。
'''

#--------#
'''
df['floats'] = (1.5, 2.5, 3.5, 4.5) # 添加一列
print(f"\n{df}")
print(f"\n{df['floats']}")
'''

#-------# 使用整个DataFrame对象来定义一个新列:

df['names'] = pd.DataFrame(['Yves', 'Sandra', 'Lilli', 'Henry'],
                          index=['d', 'a', 'b', 'c'])
print(f"\n{df}")

#-------# 添加数据：
'''
df.append({'numbers': 100, 'floats': 5.75, 'names': 'Jil'}, # append方法用于在DataFrame的末尾添加一行数据。
          ignore_index=True) # ignore_index=True表示忽略原来的索引，重新生成新的索引。
          # append 这个方法已经被弃用了，新的方法是 concat，如下👇
'''
'''

new_data = {'numbers':100, 'floats':5.75, 'names':'Jil'} # 创建一个字典
new_df = pd.DataFrame([new_data])  # 注意将字典放入列表中
result = pd.concat([df, new_df], ignore_index=True) # 将新数据添加到DataFrame中

print(f"\n{result}")
'''

# concat的正确用法👇：
# 创建要添加的新DataFrame
new_data = {'numbers':100, 'floats':5.75, 'names':'Jil'} # 创建一个字典
new_df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
print(f"\n{new_df}")

'''
# concat的正确用法👇：
# 创建要添加的新DataFrame
new_data = pd.DataFrame({'names':['Liz']}, index=['z'])

# 正确合并方式
df = pd.concat([df, new_data], sort=False)
print(f"\n{df}")
'''

print(df.dtypes)

print("\n")

print(new_df[['numbers', 'floats']].mean()) # 计算每列的平均值
print(new_df[['numbers', 'floats']].std()) # 计算每列的标准差