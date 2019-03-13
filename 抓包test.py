# -*- coding: utf-8 -*-
# @Author: Du Jun


import requests,time,re
from requests.exceptions import RequestException

url = "http://click.tool.hexun.com/click.aspx?articleid=1460918&blogid=63421037"
print('url',url)
headers = {
    'Referer':'http://lfkls.blog.hexun.com/1460918_d.html',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
res = requests.get(url,headers=headers)
if res.status_code == 200:
    data=res.text
    print(data)
    aaa = re.compile('articleClickCount.*?= (.*?);', re.S).findall(data)[0]
    print(aaa)
    bbb=re.compile('articleCommentCount.*?= (.*?);', re.S).findall(data)[0]
    print(bbb)
else:
    print('error')

