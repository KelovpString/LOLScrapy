# coding=utf-8
from apiMain import *
import pymysql
import demjson

conn = pymysql.connect(host = 'localhost',user = 'root',password = '699307', db = 'lol', charset = 'utf8')
cur = conn.cursor()
cur.execute("USE lol")

#插入地区信息
def inner_region_part():
    sql = "INSERT INTO basedata_region(xin_id,name,icon) VALUES(\"%s\",\"%s\",\"%s\")"
    list = get_region_part()
    for i in range(0,len(list)):
        temp = demjson.decode(list[i])
        cur.execute(sql,(temp['id'],temp['name'],temp['icon']))
        cur.connection.commit()

#更新 -Main
try:
    inner_region_part()
finally:
    cur.close()
    conn.close()