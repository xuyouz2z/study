import requests
from lxml import etree

herders = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
resp = requests.get("https://www.qb5.me/top/monthvisit/", headers=herders)

print(resp.text)
# 发送请求
# 接受服务器给的响应
e = etree.HTML(resp.text)
types = e.xpath('/html/body/div[@id='main']/div[@id='articlelist']/ul[2 ]/li[2]')
print(types)
