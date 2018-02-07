# coding=utf-8
#测试数据的地方 upload前 请清空源码
import json
import demjson
import pymysql

list = [u'{"id":11,"name":"Rookie","team":"iG","icon":"http://www.carry6.com/css/images/tx/Rookie.png","region":"http://static.a.carry6.com/img/nationality/49.png"}', u'{"id":67,"name":"Ruo","team":"M3","icon":"http://img.carry6.com//2016/01/11/1/60ef3938ba06934bf08b07927fb48251.jpg","regionId":81,"region":"http://static.a.carry6.com/img/nationality/81.png"}', u'{"id":355,"name":"Raison","team":"WE","icon":"http://static.a.carry6.com/img/player/355.jpg","regionId":None,"region":"http://static.a.carry6.com/img/nationality/null.png"}', u'{"id":422,"name":"Raphael","team":"M3","icon":"http://www.carry6.com/css/images/tx/Raphael.png","regionId":49,"region":"http://static.a.carry6.com/img/nationality/49.png"}', u'{"id":435,"name":"Romantic","team":"EPA","icon":"http://img.carry6.com//2016/01/19/1/49079a7baea45262da3c0b7b346e6042.jpg","regionId":81,"region":"http://static.a.carry6.com/img/nationality/81.png"}', u'{"id":543,"name":"RylUnicon","team":"\u7687\u65cf","icon":"http://img.carry6.com//2016/01/18/1/c20ab2775f937dd35fcc9aac2a951e83.jpg","regionId":81,"region":"http://static.a.carry6.com/img/nationality/81.png"}', u'{"id":724,"name":"Republic","team":"GT","icon":"http://www.766.com/css/images/tx/republic1.jpg","regionId":49,"region":"http://static.a.carry6.com/img/nationality/49.png"}', u'{"id":912,"name":"Rabbit97","team":"EPA","icon":"http://img.carry6.com//2016/01/17/1/233741f6be5459b15cebebd1e8c40ab9.png","regionId":81,"region":"http://static.a.carry6.com/img/nationality/81.png"}', u'{"id":1050,"name":"Rain","team":"iG","icon":"http://www.766.com/css/Rain1.png","regionId":49,"region":"http://static.a.carry6.com/img/nationality/49.png"}', u'{"id":1128,"name":"Road","team":"IM","icon":"http://www.766.com/css/S6/LPL/IM_Road_20160902_25A9592.png","regionId":49,"region":"http://static.a.carry6.com/img/nationality/49.png"}', u'{"id":1175,"name":"Rehope","team":"ING","icon":"http://img.carry6.com//2016/01/11/1/60ef3938ba06934bf08b07927fb48251.jpg","regionId":49,"region":"http://static.a.carry6.com/img/nationality/49.png"}', u'{"id":1223,"name":"Raes","team":"Chiefs","icon":"http://img.carry6.com//2016/01/11/1/60ef3938ba06934bf08b07927fb48251.jpg","regionId":93,"region":"http://static.a.carry6.com/img/nationality/93.png"}']

temp = demjson.decode(list[4])
sql = "INSERT INTO basedata_player(game_name)" \
          "VALUES(%s)"
conn = pymysql.connect(host = 'localhost',user = 'root',password = '699307', db = 'lol', charset = 'utf8')
cur = conn.cursor()
cur.execute("USE lol")

add = []
add.append(temp['team'])
print add
# cur.execute(sql,str(temp['name']))
# cur.connection.commit()
# a = json.loads("{\"a\":1}")
# b = a.get("c")
# if b is None:
#     b = 0
# else:
#     b = 1
print temp['team']
#if temp['regionId'] is None:
#    print "asdasd"
cur.close()
conn.close()