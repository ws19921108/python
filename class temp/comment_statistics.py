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


MAXNUM = 300

boardDict = {u'news3_bbs': '滚动新闻', u'health3_bbs': '健康3', u'mobile_bbs': '手机', u'news2_bbs': '新闻中心',
           u'news_guonei8_bbs': '国内', u'dy_wemedia_bbs': '网易号', u'video_bbs': '视频', u'money_bbs': '财经',
           u'game_bbs': '游戏', u'news_shehui7_bbs': '社会', u'news_guoji2_bbs': '国际', u'photoview_bbs': '图片',
           u'tech_bbs': '科技', u'ent2_bbs': '娱乐2', u'comment_bbs': '评论', u'news_junshi_bbs': '军事',
             u'sports2_bbs':'体育2', u'3g_bbs':'本地新闻', u'news_local_3g_bbs':'客户端', u'sports_zh_bbs':'国内体育',
             u'sports_bbs':'体育', u'tie_bbs':'跟帖', u'sports_cba_bbs':'CBA', u'sports_nba_bbs':'NBA',
             u'lady_bbs':'女人',u'gzhouse_bbs':'广州新闻', u'education_bbs':'教育',u'auto_bbs':'汽车',
             u'ent_bbs': '娱乐', u'jiankang_bbs':'健康',u'home_bbs':'家居', u'baby_bbs':'母婴', u'house_bbs':'房地产',
             u'tinyblog_bbs':'微博'}
'''
http://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/users/98845713/comments?offset=0&limit=30
http://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/users/98845713/comments?offset=0&limit=30
'''


def getBoardId(userid):
    BoardIdDict = {}
    startPos = 0
    while True:
        url = 'http://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/users/' + userid + \
              '/comments?offset=' + str(startPos) + '&limit=30'
        request = urllib2.Request(url=url)
        response = urllib2.urlopen(request, timeout=20)
        result = response.read()
        resultJson = json.loads(result)
        threads = resultJson['threads']
        total = resultJson['total']
        total = MAXNUM if total > MAXNUM else total
        for key, value in threads.items():
                boardId = value['boardId']
                # if boardId == u'auto_bbs':
                #     print value['url']
                if not boardDict.has_key(boardId):
                    boardIdCN = boardId
                else:
                    boardIdCN = boardDict[boardId]
                if boardIdCN not in BoardIdDict:
                    BoardIdDict[boardIdCN] = 1
                else:
                    BoardIdDict[boardIdCN] += 1
        startPos += 30
        if startPos > total:
            break

    boardIdList = sorted(BoardIdDict.items(), key=lambda d: d[1], reverse=True)
    return boardIdList

def eBar(myList):
    key = []
    value = []
    for item in myList:
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
    return render_template('pyecharts.html')
@app.route('/echarts/<userid>')
def echarts(userid):
    keywordsList = getBoardId(userid)
    # simpled = simpleList(keywordsList, 10)
    pie = ePie(keywordsList)
    bar = eBar(keywordsList)
    # print pie.get_js_dependencies()
    return render_template('pyecharts.html',
                           pie=pie.render_embed(),
                           bar=bar.render_embed(),
                           host=DEFAULT_HOST,
                           script_list=['echarts.min'])
if __name__ == '__main__':
    app.run()



