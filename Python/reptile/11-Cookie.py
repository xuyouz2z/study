import urllib.request, http.cookiejar

cookie = http.cookiejar.LWPCookieJar()
cookie.load(
    "D:/code/git/Python/reptile/10-cookie.txt", ignore_discard=True, ignore_expires=True
)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("https://baidu.com")
print(response.read().decode("utf-8"))
