#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://vip.stock.finance.sina.com.cn/fund_center/api/jsonp.php/IO.XSRV2.CallbackList['Il$nvMbY72HdQyks']/NetValueReturn_Service.NetValueReturnOpen?page=1&num=100&sort=form_year&asc=0&ccode=&type2=0&type3=&%5Bobject%20HTMLDivElement%5D=546oa"

import urllib2
import demjson

request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
result = response.read()

startPos = result.find('{')
jsonData = result[startPos:-2]
jsonData = jsonData.decode('gbk')
data = demjson.decode(jsonData)['data']
print len(data)

outFile = open('data\\stock data\\fund.csv','w+')
fields = []
line = ''
for key in data[0]:
    fields.append(key)
    line += key + ','
line += '\n'

outFile.write(line)


for item in data:
    line = ''
    for field in fields:
        line += str(item[field]) + ','
    line += '\n'
    outFile.write(line)

outFile.close()
