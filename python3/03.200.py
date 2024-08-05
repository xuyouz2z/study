# import urllib.request

# response = urllib.request.urlopen("https://www.python.org")
# # 响应的状态码
# print(response.status)
# # 响应头信息
# print(response.getheaders())
# # Server
# print(response.getheader("Server"))

import urllib.request

response = urllib.request.urlopen("https://www.baidu.com/")
print(response.getheader("Server"))
