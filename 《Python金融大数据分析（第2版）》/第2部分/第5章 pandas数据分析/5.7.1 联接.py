import pandas as pd
import numpy as np

data = np.random.standard_normal((10, 2))# 生成10行2列的随机数， standard_normal表示标准正态分布，
                                        # 标准正态分布意思是均值为0，方差为1的正态分布
df = pd.DataFrame(data, columns=['x', 'y'])# 将数据'data' 转换为DataFrame格式, columns=['x', 'y']表示列名
                # DataFrame格式是pandas库中的一种数据结构，类似于Excel表格，
                # 特点是有行和列，可以存储各种类型的数据，如整数、浮点数、字符串等

print(df)
print('\n')

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

# 开始联接操作：
print(df_1._append(df_2, sort=False))            # sort=False 表示不排序
print('\n')

print(df_1._append(df_2, ignore_index=True, sort=False))
                    # ignore_index=True 表示忽略原来的索引，重新生成索引, sort=False 表示不排序
print('\n')

print(pd.concat((df_1, df_2), sort=False)) # concat表示联接，(df_1, df_2)表示要联接的两个DataFrame
print('\n')

print(pd.concat((df_1, df_2), ignore_index=True, sort=False))
                    # ignore_index=True 表示忽略原来的索引，重新生成索引, sort=False 表示不排序

# 总结：
# ‼️ _append()和concat()都是联接操作，区别在于_append()只能联接两个DataFrame，而concat()可以联接多个DataFrame。
# ignore_index=True 表示忽略原来的索引，重新生成索引, sort=False 表示不排序

# wo : ‼️ 那么_append()就没有必要用了不是吗？直接用concat不就行了？

'''ChatGPT:

append() 已被弃用（deprecated）：
从 Pandas 1.4 开始，DataFrame.append() 就被标记为弃用（DeprecationWarning）。
从 Pandas 2.0 起，append() 已被彻底移除，官方建议全部用 pd.concat()。

性能差异：
对于少量数据，append() 和 concat() 没明显区别。
对于多次追加，append() 会因为多次拷贝对象而慢很多，而 concat() 一次性合并更高效。
'''