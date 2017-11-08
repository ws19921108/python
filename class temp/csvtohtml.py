#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap
import random
from pyecharts import Scatter3D
from pyecharts.constants import DEFAULT_HOST


app = Flask(__name__)
bootstrap = Bootstrap(app)

def get_from_csv(filename):
    hyList = []
    inFile = open(filename,'r')
    for line in inFile:
        item = line.split(',')
        if len(item) < 2:
            continue
        hyList.append(item)
    inFile.close()
    return hyList

def merge_list(tbList):
    tbDict = {}
    for item in tbList:
        if item[0] not in tbDict:
            tbDict[item[0]] = []
        tbDict[item[0]].append(item)
    return tbDict


def scatter3d():
    data = [generate_3d_random_point() for _ in range(80)]
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    scatter3D = Scatter3D("3D scattering plot demo", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    return scatter3D


def generate_3d_random_point():
    return [random.randint(0, 100),
            random.randint(0, 100),
            random.randint(0, 100)]


@app.route('/')
def index():
    hyList = get_from_csv('data\\stock data\\hy.csv')
    fields = hyList.pop(0)
    return render_template('index.html', fields=fields, hyList=hyList)


@app.route('/ec')
def echart():
    s3d = scatter3d()
    return render_template('echart.html',
                           myechart=s3d.render_embed(),
                           host=DEFAULT_HOST,
                           script_list=s3d.get_js_dependencies())


@app.route('/gg/<filename>')
def showgg(filename):
    ggList = get_from_csv('data\\stock data\\'+filename)
    fields = ggList.pop(0)
    return render_template('showgg.html',fields=fields,ggList=ggList)

@app.route('/tb')
def showtb():
    tbList = get_from_csv('data\\stock data\\tb.csv')
    fields = tbList.pop(0)
    tbDict = merge_list(tbList)
    return render_template('showtb.html',fields=fields,tbDict=tbDict)

@app.route('/jj')
def showjj():
    jjList = get_from_csv('data\\stock data\\fund.csv')
    fields = jjList.pop(0)
    return render_template('showjj.html',fields=fields,jjList=jjList)

if __name__ == '__main__':
    app.run()

