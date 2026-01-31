import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 生成随机日期序列
def random_dates(start, end, n=100):
    start_u = start.timestamp()
    end_u = end.timestamp()
    return [datetime.fromtimestamp(random.uniform(start_u, end_u)) for _ in range(n)]

# 生成股票代码
def random_stock_code():
    return 'STK' + str(random.randint(1000, 9999))

# 随机生成金融数据
np.random.seed(42)  # 固定随机种子，保证结果可复现
data = []
for _ in range(100):
    date = random.choice(pd.date_range('2024-01-01', '2024-12-31'))
    stock = random_stock_code()
    open_price = round(random.uniform(10, 100), 2)
    close_price = round(open_price * random.uniform(0.95, 1.05), 2)
    high = round(max(open_price, close_price) * random.uniform(1.00, 1.05), 2)
    low = round(min(open_price, close_price) * random.uniform(0.95, 1.00), 2)
    volume = random.randint(1000, 1000000)
    daily_return = round((close_price - open_price) / open_price, 4)
    data.append([date, stock, open_price, close_price, high, low, volume, daily_return])

# 创建 DataFrame
df = pd.DataFrame(data, columns=[
    '日期', '股票代码', '开盘价', '收盘价', '最高价', '最低价', '成交量', '日收益率'
])

# 保存 Excel 文件
df.to_excel('finance_data.xlsx', index=False)
print("✅ 已生成金融数据文件：finance_data.xlsx")
print(df.head())
