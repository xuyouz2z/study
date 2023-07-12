import urllib.request

response = urllib.request.urlopen("https://www.python.org")
# response = urllib.request.urlopen("https://www.python.org", data=None, timeout=0.1)
# print(response.read().decode('utf-8'))
print(type(response))
# 响应状态码
print(response.status)
# 响应头信息
print(response.getheaders())
# 调用getheaders，获取响应头中的Server值，nginx是用Nginx搭建的
print(response.getheader("Server"))
print(response.getheader("Via"))
