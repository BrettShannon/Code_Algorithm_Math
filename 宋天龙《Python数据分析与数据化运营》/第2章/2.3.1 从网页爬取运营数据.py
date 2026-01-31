import requests # 导入requests库
'''

url = 'https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91' # 定义要爬取的网页链接
res = requests.get(url) # 发送请求
html = res.text # 获取网页源代码
print(html) # 输出网页源代码
'''

# requests.get()方法发送一个GET请求，并将响应内容保存在res对象中。
# 然后，通过res.text属性获取响应的文本内容，即网页的源代码。
# 最后，使用print()函数输出网页源代码。


# ChatGPT修改版本： 
import requests

url = 'https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
} 
# ‼️ ‼️ ‼️ 设置请求头，模拟浏览器访问，避免被网站反爬虫机制拦截，提高爬取成功率，
# 同时也可以伪装成真实用户访问，提高爬取成功率。

res = requests.get(url, headers=headers) # .get()方法发送一个GET请求，并将响应内容保存在res对象中。
res.encoding = 'utf-8'  # 设置编码,避免乱码.
html = res.text # 获取网页源代码

print(html[:1000])  # 只打印前1000个字符，避免控制台太乱
