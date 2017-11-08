#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
# from bs4 import BeautifulSoup
import json
from pyecharts import Bar,Pie
from flask import Flask, render_template
from pyecharts import Scatter3D
from pyecharts.constants import DEFAULT_HOST


'''
window.sportsTeamId = {
	// 英超
	yingchao:'17',
	// 意甲 
	yijia:'23',
	// 西甲
	xijia:'8',
	// 法甲
	fajia:'34',
	// 德甲
	dejia:'35',
	// 欧冠
	ouguan:'7',
	// 英超 曼联
	manlian:'35',
	// 英超 曼城
	mancheng:'17',
	// 英超 切尔西
	qieerxi:'38',
	// 英超 阿森纳
	asenna:'42',
	// 英超 利物浦
	liwupu:'44',
	// 英超 莱斯特城 莱切斯特
	laisitecheng:'31',
	// 英超 热刺 托特纳姆
	reci:'33',
	// 西甲 巴塞罗那
	basailuona:'2817',
	// 西甲 皇马 皇家马德里
	huangma:'2829',
	// 西甲 马竞 马德里竞技
	majing:'2836',
	// 西甲 塞维利亚
	saiweiliya:'2833'
}



playerOrder = {'ssb':1,'zgb':2,'pjb':4}



teamPointUrl = 'http://api.sports.126.net/api/goal/info/teamOrder_17_1.json'
'''


def getKeyWords():
    keywordsDict = {}
    url = 'http://sports.163.com/special/000587PN/newsdata_world_index.js'
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request, timeout=20)
    result = response.read().decode('gbk')
    data = json.loads(result[14:-1])
    for news in data:
        for keyword in news['keywords']:
            keyname = keyword['keyname']
            if keyname not in keywordsDict:
                keywordsDict[keyname] = 1
            else:
                keywordsDict[keyname] += 1

    keywordsList = sorted(keywordsDict.items(), key=lambda d: d[1], reverse=True)
    return keywordsList

def eBar(myList):
    key = []
    value = []
    for item in myList[:-1]:
        key.append(item[0])
        value.append(item[1])
    bar = Bar("Keywords")
    bar.add("热词", key, value, mark_point=["max", "min"])
    return bar

def ePie(myList):
    key = []
    value = []
    for item in myList:
        key.append(item[0])
        value.append(item[1])
    pie = Pie("")
    pie.add("热词", key, value, is_label_show=True,is_legend_show=True,label_text_color=None,legend_orient='vertical', legend_pos='left')
    return pie


def simpleList(myList,num):
    simple = []
    others = 0
    for i in range(len(myList)):
        if i < num:
            simple.append(myList[i])
        else:
            others += myList[i][1]
    simple.append(('others',others))
    return simple


app = Flask(__name__)
@app.route('/')
def index():
    keywordsList = getKeyWords()
    simpled = simpleList(keywordsList, 10)
    pie = ePie(simpled)
    bar = eBar(simpled)
    # print pie.get_js_dependencies()
    return render_template('pyecharts.html',
                           pie=pie.render_embed(),
                           bar=bar.render_embed(),
                           host=DEFAULT_HOST,
                           script_list=['echarts.min'])
if __name__ == '__main__':
    app.run()




