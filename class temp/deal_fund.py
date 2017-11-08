#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import urllib2
import psycopg2
# url = 'http://stock.finance.sina.com.cn/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?symbol=003803&page=2'

'''
state:
0-空仓
1-买进
2-满仓
3-卖出
'''

#
# UP_RATE = 0.1
# DOWN_RATE = 0.1
IN_RATE = 0.9988
OUT_RATE = 0.995

conn = psycopg2.connect("dbname=postgres user=postgres")
cur = conn.cursor()

def create_table(symbol):
    sql = "CREATE TABLE t%s (id serial PRIMARY KEY, tdate date, value real)" % symbol
    # print sql
    cur.execute(sql)

    conn.commit()

def add_data(symbol,tdate, value):
    sql = "INSERT INTO t%s (tdate, value) VALUES ('%s', %s)" % (symbol, tdate, value)
    # print sql
    cur.execute(sql)
    conn.commit()




def get_fund_data_to_db(symbol):
    page = 1
    total_num = -1
    while True:
        url = 'http://stock.finance.sina.com.cn/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?symbol=' + symbol + '&page=' + str(page)
        request = urllib2.Request(url=url)
        response = urllib2.urlopen(request, timeout=20)
        result = response.read()
        result = json.loads(result)['result']
        if total_num < 0:
            total_num = int(result['data']['total_num'])
            # print total_num
        data = result['data']['data']
        if len(data) > 20:
            data.pop(-1)
        for item in data:
            tdate = item['fbrq'].split()[0]
            value = item['jjjz']
            add_data(symbol, tdate, value)
        if page*20 > total_num:
            break
        page += 1

def get_fund_from_db(symbol):
    sql = "SELECT tdate,value FROM t%s ORDER BY tdate ASC" % symbol
    cur.execute(sql)
    rows = cur.fetchall()
    return rows


def deal_fund_by_maxmin(symbol,up_rate,down_rate):
    money = 10000
    rows = get_fund_from_db(symbol)
    in_price = rows[1][1]
    fund_num = money * IN_RATE / in_price
    minValue = maxValue = in_price
    state = 2
    for row in rows:
        value = row[1]
        if state == 3:
            state = 0
            money = fund_num * value * OUT_RATE
            # print 'out:', row[0], value, fund_num, money
            fund_num = 0
        elif state==1:
            in_price = value
            fund_num = money * IN_RATE / in_price
            minValue = maxValue = value
            state = 2
            # print 'in:', row[0], value, fund_num
        if value > maxValue:
            maxValue = value
        elif value < minValue:
            minValue = value
        else:
            t_up_rate = (value - minValue) / minValue
            t_down_rate = (maxValue - value) / maxValue
            if state==2 and t_down_rate > down_rate:
                state = 3
                print 'outing:', row[0], value
            elif state == 0 and t_up_rate > up_rate:
                state = 1
                print 'inning:', row[0], value

    if fund_num:
        latest_price = rows[-1][1]
        money =  fund_num * latest_price * OUT_RATE
    return money

def clac_best_rate(symbol):
    max_money = 0
    max_up_rate = 0
    max_down_rate = 0
    for i in range(1,101):
        for j in range(1,101):
            up_rate = i/100.0
            down_rate = j/100.0
            money = deal_fund_by_maxmin(symbol,up_rate,down_rate)
            if money > max_money:
                max_money =money
                max_up_rate = up_rate
                max_down_rate = down_rate
            # print up_rate, down_rate, money

    return max_up_rate, max_down_rate, max_money


#
# sql = "CREATE TABLE best_rate (id serial PRIMARY KEY, symbol varchar, up_rate real, down_rate real)"
# # print sql
# cur.execute(sql)
# conn.commit()

#
# url = 'http://money.finance.sina.com.cn/d/api/openapi_proxy.php/?__s=[[%22jjhq%22,1,40,%22%22,0,%22lof_hq_fund%22]]'
# request = urllib2.Request(url=url)
# response = urllib2.urlopen(request, timeout=20)
# result = response.read()
# items = json.loads(result)[0]['items']

#
# for item in items:
#     symbol = item[0][2:]
#     # create_table(symbol)
#     # get_fund_data_to_db(symbol)
#     # result = clac_best_rate(symbol)
#     # sql = "INSERT INTO best_rate (symbol, up_rate, down_rate) VALUES (%s, %s, %s)" % (symbol, result[0], result[1])
#     #  print sql
#     # cur.execute(sql)
#     # conn.commit()
#     print deal_fund_by_maxmin(symbol, 0.03, 0.03)
#160215

symbol = '160215'
# create_table(symbol)
# get_fund_data_to_db(symbol)
# print clac_best_rate(symbol)

print deal_fund_by_maxmin(symbol, 0.05, 0.05)

cur.close()
conn.close()