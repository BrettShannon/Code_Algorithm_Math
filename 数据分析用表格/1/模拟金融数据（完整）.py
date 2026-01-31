import pandas as pd
import numpy as np

# 设置随机种子
np.random.seed(42)

# 生成日期序列（100天）
dates = pd.date_range(start='2025-01-01', periods=120, freq='B')  # B=工作日

# 模拟收盘价（随机游走）
close = [100]  # 起始价100
for _ in range(1, len(dates)):
    change = np.random.normal(0, 1)  # 每日波动 ~ N(0,1)
    close.append(close[-1] * (1 + change/100))  # 百分比波动

close = np.array(close).round(2)

# 开盘价、最高价、最低价
open_price = (close * (1 + np.random.normal(0, 0.002, len(close)))).round(2)
high = np.maximum(open_price, close) * (1 + np.random.uniform(0, 0.01, len(close)))
low = np.minimum(open_price, close) * (1 - np.random.uniform(0, 0.01, len(close)))
high = high.round(2)
low = low.round(2)

# 成交量（随机在1万到5万之间）
volume = np.random.randint(10000, 50000, len(close))

# 收益率
returns = np.zeros(len(close))
returns[1:] = np.diff(close) / close[:-1]

# 构建DataFrame
df = pd.DataFrame({
    "日期": dates,
    "开盘价": open_price,
    "最高价": high,
    "最低价": low,
    "收盘价": close,
    "成交量": volume,
    "收益率": returns.round(4)
})

# 保存Excel
df.to_excel("模拟金融数据.xlsx", index=False)

print("已生成Excel文件：模拟金融数据.xlsx")
