import urllib.request

url = 'https://www.baidu.com/'

proxy_support = urllib.request.ProxyHandler({'http':'121.237.149.12:3000'})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')]
response = opener.open(url)
html = response.read().decode('utf-8')
