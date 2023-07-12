from urllib import request,error

try:
    request = request.urlopen('https://cuiqingcai,com/404')
except error.URLError as e:
    print(e.reason)