from urllib.parse import urlparse

# urllib.parse.urlparse(urlstring,scheme='',alow_fragments=True)
# 其中 urlstring=待解析URL，scheme=默认协议，alow_fragments=
result = urlparse("http://baidu.com/index.html;user?id=5#comment", scheme="https")
# result = urlparse('https://baidu.com/index.html;user?did=5#coment',scheme='https')
print(result)
