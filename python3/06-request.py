import urllib.request
import gzip


# def ungzip(responsee):
#     try:
#         responsee = gzip.decompress(responsee)
#     except:
#         pass
#     return responsee


request = urllib.request.Request("https://python.org")
response = urllib.request.urlopen(request)
# buff = response.read()
# f = gzip.GzipFile(fileobj=buff)
# htmls = f.read().decode("utf-8")
# print(htmls)

# responsee = response.read().decode("utf-8")
# print(responsee)
print(response.read())  #! .decode("utf-8")???
