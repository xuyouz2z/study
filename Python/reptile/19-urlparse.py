from urllib.parse import urlparse

result = urlparse("https://baidu.com/index.html#comment", allow_fragments=False)
print(result)
print(result.scheme, result[0], result.netloc, result[1], sep="\n")
