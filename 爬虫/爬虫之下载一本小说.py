# 导入爬虫用到的模块
import urllib.request
# 导入正则表达式用到的模块
import re
# 原小说所在的url(网址)
url = 'https://www.readnovel.com/book/3733246204967801#Catalog'
# 读取
response = urllib.request.urlopen(url)
html = response.read()
html = html.decode()
# 获取小说标题
title = re.findall(r'<title>(.*?)</title>',str(html))[0][0:12]
with open(f'{title}.txt','w',encoding='utf-8') as file_obj:
    # dl = re.findall(r'<ul class="cf">.*?</ul>',html,re.S)
    chapter_list1 = re.findall(r'href="(.*?)" target="_blank" data-cid',str(html))
    chapter_list2 = re.findall(r'章节字数：.*?>(.*?)<',str(html))
    chapter_list = []
    for i in range(len(chapter_list1)):
        chapter_list.append((chapter_list1[i],chapter_list2[i]))
    for chapter_info in chapter_list:
        chapter_url,chapter_title = chapter_info
        chapter_url = 'https:%s'%chapter_url
        chapter_response = urllib.request.urlopen(chapter_url)
        chapter_html = chapter_response.read().decode('utf-8')
        # 提取章节内容
        chapter_content = re.findall(r'<div class="read-content j_readContent">(.*?)</div>',chapter_html,re.S)[0]
        chapter_content = chapter_content.replace(' ','')
        chapter_content = chapter_content.replace('<p>','')
        chapter_content = chapter_content.replace('\n','')
        # 将内容下载到txt文件中
        file_obj.write(chapter_title)
        file_obj.write('\n')
        file_obj.write(chapter_content)
        file_obj.write('\n')
        print(chapter_url)