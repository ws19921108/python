#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib
import urllib2
from bs4 import BeautifulSoup
import json
import matplotlib.pyplot as plt
from datetime import datetime
# url = 'http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013'
# #Get
# request = urllib2.Request(url=url)
# response = urllib2.urlopen(request)
# result = response.read()


url = 'http://shuju.wdzj.com/plat-info-target.html'
# dataDict = {'target2': 0, 'target1': 2, 'type': 1, 'wdzjPlatId': 59}
# data = json.dumps(dataDict)
# print type(data)
# print data
# data = urllib.urlencode({'target2': 0, 'target1': 2, 'type': 1, 'wdzjPlatId': 59})
# print type(data)
# print data
data = 'type=1&wdzjPlatId=59&target2=0&target1=2'
#Post
request = urllib2.Request(url=url)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
response = opener.open(request,data)
result = response.read()

resultJson = json.loads(result)
date = resultJson['date']
data1 = resultJson['data1']

for i in range(len(date)):
    date[i] = datetime.strptime(date[i],'%Y-%m-%d')

plt.plot_date(x=date, y=data1, linestyle="-", marker="None")
plt.show()