import MySQLdb
import  MySQLdb.cursors
db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db='douban', port=3306, charset='utf8', cursorclass = MySQLdb.cursors.DictCursor)
db.autocommit(True)
cursor = db.cursor()

# #create
# inFile = open('data\\douban_movie_clean.txt','r')
# count = 0
# for line in inFile:
#     count += 1
#     if count == 1:
#         continue
#     line = line.strip().split('^')
#     cursor.execute('insert into movie(title, url, rate, length, description) values(%s, %s, %s, %s, %s)', [line[1], line[2], line[4], line[-3],line[-1]])
#     if count == 5:
#         break
# inFile.close()

# #update
# cursor.execute('update movie set title=%s, length=%s where id=1',['update movie', 99])

# #read
# cursor.execute('select title, length from movie where id = 1')
# movie = cursor.fetchall()
# print movie[0]
# # movie = cursor.fetchone()
# #print movie


#delete
cursor.execute('delete from movie WHERE id=%s',[1])

cursor.close()
db.close()