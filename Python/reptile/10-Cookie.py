import urllib.request, http.cookiejar

filename = 'D:/code/git/Python/reptile/10-cookie.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
# cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)