from urllib.parse import urlparse

# urllib.parse.urlparse(urlstring,scheme='',alow_fragments=True)
# 其中 urlstring=待解析URL，scheme=默认协议，alow_fragments=是否忽略fragment
result = urlparse("https://baidu.com/index.html;user?id=5#comment")
# result = urlparse('https://baidu.com/index.html;user?did=5#comment',scheme='https')
print(result)
