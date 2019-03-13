# -*- coding: utf-8 -*-
# @Author: Du Jun

import re,requests

url='http://18517180.blog.hexun.com/118347384_d.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.3'}
data=requests.get(url=url,headers=headers).text
# print(data)
pat_blog_id='http://cache-sidebar.blog.hexun.com/inc/ARecommend.aspx\?blogid=(.*?)&articleids=(.*?)&'
aaa=re.compile(pat_blog_id,re.S).findall(data)[0]
print(aaa[0],aaa[1])