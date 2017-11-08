#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://finance.sina.com.cn/fund/fundnew.html'

import urllib2
from bs4 import BeautifulSoup

request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=20)
result = response.read().decode('gbk')
soup = BeautifulSoup(result,"html.parser")
table =  soup.find('tbody',id='tbody_list_0')

outFile = open('data\\stock data\\newfund.csv','w+')
colomns = table.find_all('tr')
for colomn in colomns:
    line = ''
    rows = colomn.find_all('th')
    for row in rows:
        line += row.text.strip() .replace("\n", "") + ','
    line += '\n'
    outFile.write(line)
outFile.close()

# outFile = open('data\\stock data\\fund.csv','w+')
# fields = []
# line = ''
# for key in data[0]:
#     fields.append(key)
#     line += key + ','
# line += '\n'
#
# outFile.write(line)
#
#
# for item in data:
#     line = ''
#     for field in fields:
#         line += str(item[field]) + ','
#     line += '\n'
#     outFile.write(line)
#
# outFile.close()
