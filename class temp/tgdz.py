#coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


tianGanList = ['甲','已','丙','丁','戊','己','庚','辛','壬','癸']
diZhiList = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']


year = 2017

yTianGan = year%10 - 4
yDiZhi = year%12 -4

oldYear = tianGanList[yTianGan]+diZhiList[yDiZhi]

print oldYear

# month = 7 #闰月问题比较麻烦
#
# mTianGan = (yTianGan + month + 3) % 10
# mDiZhi = (yDiZhi + month + 3) % 12
#
# oldMonth = tianGanList[mTianGan]+diZhiList[mDiZhi]

# print oldMonth