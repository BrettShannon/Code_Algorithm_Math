'''
url = 'https://api.github.com/repos/.pandas-dev/pandas/issues'

'''

# 传递数据到DataFrame，并提取感兴趣的字段：
import pandas as pd
import requests

issues = pd.DataFrame(data, columns=['number', 'title',
                                     'labels', 'state'])
# 提取标签列表：
print(issues)

