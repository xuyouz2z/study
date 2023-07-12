from urllib.parse import urlparse

result = urlparse("https://baidu.com/index.html;user?id=5#comment")
print(type(result))
print(result)
# scheme=协议   netloc=域名 .....
