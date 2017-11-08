#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap
from pyecharts import Scatter3D
from pyecharts.constants import DEFAULT_HOST
import urllib2
import json
import psycopg2
from datetime import date


app = Flask(__name__)
bootstrap = Bootstrap(app)
conn = psycopg2.connect("dbname=postgres user=postgres")
cur = conn.cursor()
day = date.today().strftime("%d%m%y")

def store_top_bill():
    url = 'http://money.finance.sina.com.cn/d/api/openapi.php/CN_Bill.getBillTopListByDay'
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request, timeout=20)
    result = response.read().decode('gbk')
    # print result
    data = json.loads(result)['result']['data']
    fields = data['fields']
    table_name = 'top_bill' + day
    # table_name = 't501000'
    sql = "SELECT tablename FROM pg_tables WHERE schemaname='public' AND tablename='%s'" % table_name
    cur.execute(sql)
    res =  cur.fetchone()
    if res:
        sql = "DROP TABLE %s" % table_name
        cur.execute(sql)
    sql = "CREATE TABLE %s (id serial PRIMARY KEY, symbol varchar, name varchar, ticktime time, price real, volume integer, prev_price real, kind varchar, settlement real, ratio_avg_volume_20 integer)" \
          % table_name
    cur.execute(sql)

    for item in data['items']:
        sql = "INSERT INTO %s (symbol, name, ticktime, price, volume, prev_price, kind, settlement, ratio_avg_volume_20) VALUES ('%s', '%s',  '%s', %s, %s, %s, '%s', %s, %s)"\
              % ((table_name,) + tuple(item))
        cur.execute(sql)
    conn.commit()

def get_top_bill_all(table_name):
    sql = "SELECT * FROM %s" % table_name
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

def get_top_bill_symbol(table_name):
    sql = "SELECT symbol FROM %s GROUP BY symbol" % table_name
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

def get_top_bill_by_symbol(table_name, symbol):
    sql = "SELECT * FROM %s WHERE symbol='%s'" % (table_name, symbol)
    cur.execute(sql)
    rows = cur.fetchall()
    return rows




if __name__ == '__main__':
    # store_top_bill()
    table_name = 'top_bill'+day
    symbol = 'sz000100'
    # print get_top_bill_all(table_name)
    # print get_top_bill_symbol(table_name)
    # print get_top_bill_by_symbol(table_name, symbol)
    app.run()

    cur.close()
    conn.close()