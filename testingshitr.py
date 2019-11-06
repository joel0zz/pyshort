from urllib.parse import urlparse

x = urlparse("ertgfdghrgffghgf")
print(x)
if x.scheme and x.netloc is not None:
    print("is url")
else:
    print("not asshole")