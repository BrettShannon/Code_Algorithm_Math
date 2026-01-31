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

c = pd.Series([250, 150, 50], index=['b', 'd', 'c'])    # 创建Series,索引为b,d,c,值为250,150,50,
                                        # Series是一维数据，可以看作是特殊的字典，  索引为键，值为值，  
                                        # Series的索引默认为整数索引，从0开始，可以自定义索引。
df_1['C'] = c # 将Series赋值给DataFrame的C列
df_2['C'] = c # 将Series赋值给DataFrame的C列

print(df_1)
print('\n')
print(df_2)
print('\n')

print(pd.merge(df_1, df_2,)) # 默认按照索引合并,合并结果为两个DataFrame的‼️交集部分,即索引为b,d的行
print('\n')

print(pd.merge(df_1, df_2, on='C'))  # 按照C列合并,合并结果为两个DataFrame的‼️交集部分,即值为250,150,50的行
print('\n')

print(pd.merge(df_1, df_2, how='outer')) # 按照索引合并,合并结果为两个DataFrame的并集部分,即索引为a,b,c,d,f的行
                                        # how='outer'表示合并方式为外连接，即保留两个DataFrame的所有行，
                                        # 如果某个行在另一个DataFrame中不存在，则用NaN填充

print('\n')
print(pd.merge(df_1, df_2, how='inner')) # 按照索引合并,合并结果为两个DataFrame的‼️交集部分,即索引为b,d的行

print('\n')

print(pd.merge(df_1, df_2, left_on='A', right_on='B')) 
                         # 按照A列和B列合并,合并结果为两个DataFrame的‼️交集部分,即值为200的行
                         # left_on和right_on分别表示左表和右表的连接列
print('\n')

print(pd.merge(df_1, df_2, left_on='A', right_on='B', how='outer')) 
                            # 按照A列和B列合并,合并结果为两个DataFrame的并集部分,即索引为a,b,c,d,f的行
print('\n')

print(pd.merge(df_1, df_2, left_index=True, right_index=True)) 
                            # 按照索引合并,合并结果为两个DataFrame的‼️交集部分,即索引为b,d的行
                            # left_index和right_index分别表示左表和右表的索引列
print('\n')
print(pd.merge(df_1, df_2, on='C', left_index=True))
                                    # 按照C列合并,合并结果为两个DataFrame的‼️交集部分,即值为250,150,50的行
                                    # left_index=True表示左表的索引列作为连接列
                                    # on表示连接列
print('\n')
print(pd.merge(df_1, df_2, on='C', right_index=True))
                                    # 按照C列合并,合并结果为两个DataFrame的‼️交集部分,即值为250,150,50的行
                                    # right_index=True表示右表的索引列作为连接列
print('\n')
print(pd.merge(df_1, df_2, on='C', left_index=True, right_index=True))
                                    # 按照C列合并,合并结果为两个DataFrame的‼️交集部分,即值为250,150,50的行
                                    # left_index=True表示左表的索引列作为连接列
                                    # right_index=True表示右表的索引列作为连接列
