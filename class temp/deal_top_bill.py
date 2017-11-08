#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
['symbol', 'name', 'ticktime', 'price', 'volume', 'prev_price', 'kind', 'settlement', 'ratio_avg_volume_20', '']
'''




money = 10000

MAX_IN = 100
stock_dict = {}
day_data = []
temp_dict = {}

import csv
import urllib2
def get_stock_value(symbol):
    url = 'http://hq.sinajs.cn/list=' + symbol
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request, timeout=20)
    result = response.read()
    price = result.split(',')[3]
    return float(price)


def calc_stock_dict(stock_dict):
    sum = 0
    for stock,value in stock_dict.items():
        price = get_stock_value(stock)
        sum += value * price
    return sum



inFile = open('data\\stock data\\tb.csv','r+')
data = csv.reader(inFile)
for item in data:
    day_data.append(item)


day_data.pop(0)
day_data.reverse()




for item in day_data:
    if item[0] not in temp_dict:
        temp_dict[item[0]] = item[6]
    elif temp_dict[item[0]] == item[6]:
        if item[6] == 'D' and item[0] in stock_dict:
            money += stock_dict[item[0]] * float(item[3])
            del stock_dict[item[0]]
            print 'out:',item[1],item[3],item[2]
        elif item[6] == 'U' and item[0]  not in stock_dict:
            stock_dict[item[0]] = MAX_IN / float(item[3])
            money -= MAX_IN
            print 'in:', item[1], item[3],item[2]
        del temp_dict[item[0]]
    else:
        temp_dict[item[0]] = item[6]


print money
calc_value =  calc_stock_dict(stock_dict)
print calc_value
print money+calc_value

# for k,v in stock_dict.items():
#     print k,v



inFile.close()


get_stock_value('sh600111')

