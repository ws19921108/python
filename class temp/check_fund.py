#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import csv

topFile = open('data\\stock data\\fund.csv','r+')
topFund = csv.reader(topFile)
topList = []
nameList = []
for item in topFund:
    topList.append(item)
    nameList.append(item[15])
nameList.pop(0)
topList.pop(0)
newFile = open('data\\stock data\\newfund.csv','r+')
newFund = csv.reader(newFile)

outFile = open('data\\stock data\\match.csv','w+')
for item in newFund:
    names = item[2].split()
    for name in names:
        for i in range(len(nameList)):
            if name in nameList[i]:
                line =  str(i)+','+name+','+item[0]+','+item[1]+','+item[4]+','+topList[i][1]+'\n'
                outFile.write(line)


topFile.close()
newFile.close()
outFile.close()