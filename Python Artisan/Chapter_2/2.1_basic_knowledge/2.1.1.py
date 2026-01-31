s = 'Hello, 中文'
print(type(s))  # <class 'str'>

# 打印中文：
print(s)  # Hello, 中文

print()

# 2.1.1

# 将浮点数转换为整型（整数）
temp = 37.2
score = 100
a = int(temp) # temp是浮点数变量
print(a)  # 37
# 将整型转换为浮点数
b = float(score) # score是整型变量
print(b)  # 100.0
print()

# 以‘千’为单位分隔数字
i = 1_000_000
i = i + 10
print(i)  # 1000010
print()

from decimal import Decimal
# 注意：这里的0.1和0.2必须是字符串
a = Decimal('0.1')
b = Decimal('0.2')
c = a + b
print(c)  # 0.3
print(type(c))  # <class 'decimal.Decimal'>
print()

# 直接使用浮点数0.1会有精度问题👇
print(Decimal(0.1))
