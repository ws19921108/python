#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json

notWord = [' ', '　', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']

fileIn = open('data\\xyj.txt','r')
staticDict = {}
for line in fileIn:
    line = line.strip()
    line = unicode(line)
    for ch in line:
        if ch in notWord:
            continue
        if ch not in staticDict:
            staticDict[ch] = 1
        staticDict[ch] += 1

staticDict = sorted(staticDict.items(),key=lambda item:item[1],reverse=True)

fileJson = open('data\\result.json','w')
fileJson.write(json.dumps(staticDict))
fileJson.close()

fileCsv = open('data\\result.csv','w')
for item in staticDict:
    fileCsv.write(item[0]+','+str(item[1])+'\n')
fileCsv.close()

fileIn.close()