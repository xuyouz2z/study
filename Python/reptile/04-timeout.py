import urllib.request
import socket
import urllib.error

try:
    response = urllib.request.urlopen('http://www.httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('timeout')