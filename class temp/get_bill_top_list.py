#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://money.finance.sina.com.cn/d/api/openapi.php/CN_Bill.getBillTopListByDay'



import urllib2
import json
from urllib import urlencode
import datetime
# import codecs


request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
result = response.read()
# print result
data = json.loads(result)['result']['data']


outFile = open('data\\stock data\\tb.csv','w+')

fields = data['fields']
line = ''
for field in fields:
    line += field + ','
line += '\n'

outFile.write(line)


for item in data['items']:
    line = ''
    for i in item:
        line += str(i) + ','
    line += '\n'
    outFile.write(line)

outFile.close()