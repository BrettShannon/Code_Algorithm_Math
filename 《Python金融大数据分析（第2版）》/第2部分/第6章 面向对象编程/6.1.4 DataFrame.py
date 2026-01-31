import pandas as pd

df = pd.DataFrame(a, columns=list('abcd'))

print(type(df))
print()

print(df.columns) # 列名
print()

print(df.sum()) # 列和
print()

print(df.cumsum()) # 累加和
print()

print(df + df) # 列相加
print()

print(df * 2) # 列乘2
print()

print(np.sum(df)) # 所有元素和
print()

print(df.__sizeof__()) # DataFrame占用的内存大小
print()

# 以下是书上没有的：
print(df.shape) # 行数和列数
print()

print(df.values) # 转为ndarray
print()

print(df.dtypes) # 列类型
print()

print(df.head()) # 前五行
print()

print(df.tail()) # 后五行
print()

print(df.describe()) # 统计信息
print()

print(df.info()) # 数据信息
print()

print(df.isnull()) # 是否为空
print()

print(df.notnull()) # 是否不为空
print()

print(df.dropna()) # 删除空值
print()

print(df.dropna(axis=1)) # 删除空值的列
print()

print(df.dropna(axis=0)) # 删除空值的行
print()

# ……