#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import psycopg2
# url = 'http://stock.finance.sina.com.cn/fundInfo/api/openapi.php/CaihuiFundInfoService.getNav?symbol=003803&page=2'

conn = psycopg2.connect("dbname=postgres user=postgres")
cur = conn.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)" , (100, "abcdef"))
cur.execute("SELECT * FROM test;")
print cur.fetchone()
conn.commit()
cur.close()
conn.close()