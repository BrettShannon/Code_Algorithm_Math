import requests
url = 'https://movie.douban.com/subject/36522427/'
res = requests.get(url)
html = res.text
print(html)

# 先看状态码：200表示成功，418表示失败
print(res.status_code) # 418

# 我现在给你一个「立刻能成功」的练习。示例网站（官方给爬的）

import requests
from bs4 import BeautifulSoup # 解析html，提取数据，

url = "https://quotes.toscrape.com/"

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml") # 解析html，提取数据

quotes = soup.select(".quote .text") # 提取数据，返回列表

for q in quotes:
    print(q.text)


'''

# 保存文件
with open('douban.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('保存成功')

# 保存图片
url = 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2549177902.webp'
res = requests.get(url)
with open('douban.jpg', 'wb') as f:
    f.write(res.content)
print('保存成功')

# 保存json
import json
url = 'https://api.douban.com/v2/movie/in_theaters'
res = requests.get(url)
data = res.json()
with open('douban.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print('保存成功')
# 保存csv
import csv
url = 'https://api.douban.com/v2/movie/in_theaters'
res = requests.get(url)
data = res.json()
with open('douban.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['电影名称', '评分', '导演', '主演', '类型', '上映时间'])
    for item in data['subjects']:
        writer.writerow([item['title'], item['rating']['average'], item['directors'][0]['name'], item['casts'][0]['name'], item['genres'][0], item['pubdate']])
print('保存成功')

# 保存xlsx
import pandas as pd
url = 'https://api.douban.com/v2/movie/in_theaters'
res = requests.get(url)
data = res.json()
df = pd.DataFrame(data['subjects'])
df.to_excel('douban.xlsx', index=False)
print('保存成功')

'''