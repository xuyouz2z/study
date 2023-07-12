import urllib.parse
import urllib.request

# 把参数name转码 使用bytes方法（该方法第一个参数是str类型）
# 模拟表单提交
data = bytes(urllib.parse.urlencode({'name':'germey'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read().decode('utf-8'))