# from导入单个函数（绝对路径）
# import导入一个文件夹（相对路径）
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler(
    {"http": "http://127.0.0.1:8080", "https": "https://127.0.0.1:8080"}
)
opener = build_opener(proxy_handler)
try:
    response = opener.open("https://www.baidu.com")
    print(response.read().decode("utf-8"))
except URLError as e:
    print(e.reason)
