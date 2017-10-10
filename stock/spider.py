#-*-coding:utf-8-*-

# http://image.sinajs.cn/newchart/min/n/sh000001.gif
# http://hq.sinajs.cn/sh000001
#http://top.baidu.com/buzz?b=1&fr=topindex

from urllib2 import urlopen
from bs4 import BeautifulSoup
from datetime import datetime




news_url = 'http://top.baidu.com/buzz?b=1&fr=topindex'
def getnews():
    news = []
    new = {}
    html = urlopen(news_url).read().decode('gbk')
    soup = BeautifulSoup(html, "html.parser")
    titles = soup.find_all('a', class_='list-title', limit=3)
    contents = soup.find_all('p', class_='info-text', limit=3)
    for title, content in zip(titles, contents):
        new['title'] = title.text
        new['content'] = content.text
        news.append(new)
        new = {}
    return news

fund_url = 'http://fund.eastmoney.com/'
def getfund(found_num):
    datas = []
    daydict = {}

    url = fund_url + found_num + '.html'
    html = urlopen(url).read()  # .decode('gb2312')
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find('li', id='Li1').div.table.find_all('tr')
    for row in rows:
        td = row.find_all('td')
        if len(td) == 4:
            daydict['day'] = td[0].text
            daydict['value'] = td[1].text
            daydict['speed'] = td[3].text
            datas.append(daydict)
            daydict = {}
    return datas

#stock_url = 'http://app.finance.china.com.cn/stock/quote/history.php?code='
def getstock(stock_num):
    datas = []
    daydict = {}

    #url = stock_url + stock_num + '&type=daily'
    url = 'http://quotes.money.163.com/trade/lsjysj_zhishu_000001.html'
    html = urlopen(url).read()  # .decode('gb2312')
    soup = BeautifulSoup(html, "html.parser")

    rows = soup.find('table', class_='table_bg001 border_box limit_sale').find_all('tr')[2:]
    for row in rows:
        td = row.find_all('td')
        date = datetime.strptime(td[0].text, '%Y%m%d')
        if date < datetime.today():
            daydict['day'] = td[0].text
            daydict['value'] = td[4].text
            daydict['speed'] = td[6].text
            datas.append(daydict)
            daydict = {}
    return datas