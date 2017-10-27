#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://money.finance.sina.com.cn/d/api/openapi_proxy.php/'

para_hy = {
    '__s':'[["swhy","amount",0]]',
    # 'callback':'var chartHangc=',
}

para_gg = {
    '__s':'[["swhy_node","sw_dz","amount",0,1,400]]',
    # 'callback':'var chartHangc='
}



import urllib2
import json
from urllib import urlencode
import datetime
# import codecs


req_url = url + '?' + urlencode(para_hy)
request = urllib2.Request(url=req_url)
response = urllib2.urlopen(request, timeout=20)
result = response.read()

data = json.loads(result)[0]

# print data

now=datetime.datetime.now()
strTime = now.strftime('%Y-%m-%d %H:%M:%S')

outFile = open('data\\stock data\\hy.csv','w+')

line = strTime + '\n'
outFile.write(line)
line = 'count:' + str(data['count']) + '\n'
outFile.write(line)
fields = data['fields']
line = ''
for field in fields:
    line += field + ','
line += '\n'

outFile.write(line)

hyList = []

for item in data['items']:
    hyDict = {}
    hyDict['name'] = item[0]
    hyDict['code'] = item[1]
    hyList.append(hyDict)
    line = ''
    for i in item:
        line += str(i) + ','
    line += '\n'
    outFile.write(line)

outFile.close()

for hy in hyList:
    para_gg['__s'] = '[["swhy_node","%s","amount",0,1,400]]' % hy['code']
    # print para_gg
    req_url = url + '?' + urlencode(para_gg)
    request = urllib2.Request(url=req_url)
    response = urllib2.urlopen(request, timeout=20)
    result = response.read()

    data = json.loads(result)[0]

    filename = 'data\\stock data\\' + hy['code'] + '.csv'
    outFile = open(filename,'w+')
    line = strTime + '\n'
    outFile.write(line)
    line = 'count:' + str(data['count']) + '\n'
    outFile.write(line)
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
