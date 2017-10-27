#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

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



@app.route('/')
def index(filename='hy.csv'):
    hyList = get_from_csv('data\\stock data\\'+filename)
    fields = hyList.pop(0)
    return render_template('index.html',fields=fields,hyList=hyList)

if __name__ == '__main__':
    app.run()