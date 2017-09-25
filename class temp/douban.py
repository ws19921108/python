#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
from bs4 import BeautifulSoup
import json

tags = []
# movies = []
url = 'https://movie.douban.com/j/search_tags?type=tv&tag=热门&source=index'
#GET
request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
result = response.read()
tags = json.loads(result)['tags']

outFile = open('data\\movies.csv', 'w')
header = 'title,url,imgurl,cover_y,is_new,rate,cover_x,playable,id,directors,writers,actors\n'
outFile.write(header)

for tag in tags:
    page_start = 0
    page_limit = 40
    while True:
        url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=' + tag + '&page_limit=' + str(page_limit) + '&page_start=' + str(page_start)
        request = urllib2.Request(url=url)
        response = urllib2.urlopen(request, timeout=20)
        result = response.read()
        subjects = json.loads(result)['subjects']
        if len(subjects) == 0:
            break
        for subject in subjects:
            line = ''
            for (key, value) in subject.items():
                line += str(value)+ ','
            # movies.append(subject)
            request = urllib2.Request(url=subject['url'])
            response = urllib2.urlopen(request, timeout=20)
            result = response.read()
            html = BeautifulSoup(result, "html.parser")
            info =  html.select('#info')[0]
            attrs = info.select('span.attrs')
            for attr in attrs:
                line += attr.get_text() + ','
            outFile.write(line[:-1] + '\n')
        page_start += page_limit

outFile.close()



#https://movie.douban.com/j/search_subjects?type=tv&tag=热门&page_limit=40&page_start=0